# use Marko to parse several code blocks

import datetime
import os
import pathlib
import random
import string
import sys
from string import Template

import frontmatter
import yaml
from marko import Markdown
from marko.block import BlockElement, FencedCode, Heading
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.lexers.go import GoLexer
from pygments.styles import get_style_by_name as get_style
from pygments.util import ClassNotFound


class TengoLexer(GoLexer):
    name = "Tengo"
    aliases = ["tengo"]


class FencedCodeGroup(BlockElement):
    """Fenced code block group: (```python\nhello\n```\n```go\nworld\n```\n)"""

    virtual = True
    priority = 8

    def _generate_id(self):
        return "".join(random.choices(string.ascii_letters, k=6))

    def __init__(self, elements):
        # self.children = []
        self.children = elements
        self.html_id = self._generate_id()


class TabbedCodeRendererMixin(object):
    def _generate_id(self):
        return "".join(random.choices(string.ascii_letters, k=6))

    def _get_lexer(self, element, code):
        lexer = None
        if element.lang:
            try:
                lexer = get_lexer_by_name(element.lang, stripall=True)
            except ClassNotFound:
                lexer = None

            if element.lang == "tengo":
                lexer = TengoLexer(stripall=True)

        if lexer is None:
            lexer = guess_lexer(code)

        return lexer

    def _get_code(self, element):
        if element.children:
            return element.children[0].children
        return ""

    def _render_tab(self, element, index):
        code = self._get_code(element)
        lexer = self._get_lexer(element, code)

        active_class = "active" if index == 0 else ""

        s = '<li class="nav-item" role="presentation">'
        s += f'<button class="nav-link {active_class}" id="{element.html_id}-tab" data-bs-toggle="tab" data-bs-target="#{element.html_id}" type="button" role="tab" aria-controls="{element.html_id}" aria-selected="true">{lexer.name}</button>'
        s += "</li>"

        return s

    def _render_content(self, element, index):
        code = self._get_code(element)
        lexer = self._get_lexer(element, code)
        formatter = html.HtmlFormatter(linenos="table")
        formatter.style = get_style("default")
        return highlight(code, lexer, formatter)

    def _render_pane(self, element, index):
        active_class = "active" if index == 0 else ""

        s = f'<div class="tab-pane {active_class}" id="{element.html_id}" role="tabpanel" aria-labelledby="{element.html_id}-tab">'
        s += self._render_content(element, index)
        s += "</div>"

        return s

    def render_fenced_code_group(self, element):
        # bootstrap 5.2 nav tabbed code

        for child in element.children:
            child.html_id = self._generate_id()

        tabs = "".join(
            [
                self._render_tab(child, index)
                for index, child in enumerate(element.children)
            ]
        )

        content = "".join(
            [
                self._render_pane(child, index)
                for index, child in enumerate(element.children)
            ]
        )

        return f"""<div class="card">
            <div class="card-header">
                <ul class="nav nav-tabs card-header-tabs" id="{element.html_id}" role="tablist">
                    {tabs}
                </ul>
            </div>
            <div class="card-body">
                <div class="tab-content" id="{element.html_id}-content">
                    {content}
                </div>
            </div>
        </div>"""


class TabbedCode:
    elements = [FencedCodeGroup]
    renderer_mixins = [TabbedCodeRendererMixin]


def main(argv):
    if len(argv) < 1 or len(argv) > 2:
        print("Usage: byexample-page <input.md> [output.html]")
        return

    def group_fenced_code_blocks(elements):
        """Group fenced code blocks into one element."""
        result = []
        for element in elements:
            if isinstance(element, FencedCode):
                if result and isinstance(result[-1], FencedCodeGroup):
                    result[-1].children.append(element)
                else:
                    result.append(FencedCodeGroup([element]))
            else:
                result.append(element)
        return result

    def get_page_title(elements, prefix=""):
        """Get page title from the first h1 element."""
        for element in elements:
            if isinstance(element, Heading) and element.level == 1:
                return (
                    element.children[0].children
                    if prefix == ""
                    else f"{prefix}: {element.children[0].children}"
                )
        return f"{prefix}: Untitled"

    def get_page_title_no_prefix(elements):
        """Get page title from the first h1 element."""
        for element in elements:
            if isinstance(element, Heading) and element.level == 1:
                return element.children[0].children
        return "Untitled"

    input_file = argv[0]
    output_file = argv[1] if len(argv) > 1 else None

    file_content = ""
    with open(input_file, "r") as f:
        post = frontmatter.load(f)
        file_content = post.content

    input_dir = os.path.dirname(input_file)

    # Check for the metadata.yaml file
    metadata_file = pathlib.Path(input_dir, "metadata.yaml")
    if metadata_file.exists():
        metadata = yaml.safe_load(metadata_file.read_text())
    else:
        # Print to stderr
        print(f"WARNING: No metadata file found at {metadata_file}", file=sys.stderr)
        metadata = {}

    markdown = Markdown(extensions=[TabbedCode, "gfm"])
    doc = markdown.parse(file_content)
    doc.children = group_fenced_code_blocks(doc.children)

    # Replace the first h1 from doc.children with the prefix and title
    # from the metadata file.
    for index, element in enumerate(doc.children):
        if isinstance(element, Heading) and element.level == 1:
            doc.children[index].children[0].children = (
                metadata.get("prefix", "") + ": " + element.children[0].children
            )
            break

    body = markdown.renderer.render(doc)
    # title = get_page_title(doc.children, prefix=metadata.get("prefix", ""))
    title = get_page_title_no_prefix(doc.children)

    p = pathlib.Path(input_file)

    # Current date on the format March 15, 2023
    todate = datetime.datetime.now().strftime("%B %d, %Y")

    with open("templates/example.html", "r") as f:
        template = Template(f.read())

    html5 = template.substitute(
        title=title,
        description=metadata.get("description", title),
        body=body,
        md_source=pathlib.Path(*p.parts[1:]),
        html_source=pathlib.Path(*p.with_suffix(".html").parts[1:]),
        last_updated=todate,
    )

    # Now, find all references to http://canary.lvh.me and replace them with https://customer.noda.se
    html5 = html5.replace("http://canary.lvh.me", "https://customer.noda.se")

    if output_file is None:
        print(html5)
    else:
        with open(output_file, "w") as f:
            f.write(html5)


if __name__ == "__main__":
    main(sys.argv[1:])
