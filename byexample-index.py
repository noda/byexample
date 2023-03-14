# Generate an index for all examples

import os
import pathlib
import sys
from string import Template

import yaml
from marko import Markdown
from marko.block import Heading

HTML5_TEMPLATE = Template(
    """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
 
    <title>$title</title>

    <link rel="icon" type="image/png" href="/favicon.png" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="/css/bootstrap.min.css">
    <link rel="stylesheet" href="/css/main.css">
</head>
<body>
    <div class="container mt-5">
        <div class="row">
            <div class="col-12">
            $body
            </div>

            <footer class="footer col-12">
                by <a href="https://www.noda.se">NODA Intelligent Systems AB</a> |
                <a href="https://github.com/noda/byexample">source</a> |
                <a href="https://github.com/noda/byexample/blob/main/LICENSE">license</a>
            </footer>
        </div>
    </div>
</body>
</html>
"""
)

MD_TEMPLATE = Template(
    """# $title

NODA provides a variety of solutions for performing advanced control of energy resources.

*NODA by Example* is a hands-on introduction intended for engineers and researchers who want to interact with our systems.

$body
"""
)


def extract_title_from_md_file(filename):
    md = Markdown()
    with open(filename, "r") as f:
        doc = md.parse(f.read())
    for element in doc.children:
        if isinstance(element, Heading) and element.level == 1:
            return element.children[0].children
    return None


def get_directory_metadata(folder):
    for dirpath, dirnames, filenames in os.walk(folder):
        # check for metadata.yaml
        if "metadata.yaml" in filenames:
            with open(os.path.join(dirpath, "metadata.yaml"), "r") as f:
                return yaml.safe_load(f.read())
    return None


def get_structure(folder):
    output = {}

    for dirpath, dirnames, filenames in os.walk(folder):
        # print(dirpath, dirnames, filenames)

        if "metadata.yaml" in filenames:
            metadata = get_directory_metadata(dirpath)
            if metadata is None:
                # print error to stderr
                print("No metadata.yaml found in {}".format(dirpath), file=sys.stderr)
                continue

            output[dirpath] = {
                "metadata": metadata,
                "examples": [],
            }

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if filename.endswith(".md"):
                p = pathlib.Path(file_path)
                output[dirpath]["examples"].append(
                    {
                        "path": pathlib.Path(*p.parts[1:])
                        .as_posix()
                        .replace(".md", ".html"),
                        "title": extract_title_from_md_file(file_path),
                    }
                )

    return output


def render_structure_as_md(structure):
    output = ""

    for dirpath, data in structure.items():
        output += "## {}\n".format(data["metadata"]["product"])
        for example in data["examples"]:
            output += "- [{}]({})\n".format(example["title"], example["path"])

    return output


def main(argv):
    if len(argv) != 1:
        print("Usage: byexample-index.py <path>")
        return

    structure = get_structure(argv[0])
    md_content = render_structure_as_md(structure)

    title = "NODA by Example"

    md = Markdown()
    content = MD_TEMPLATE.substitute(title=title, body=md_content)

    doc = md.parse(content)
    body = md.renderer.render(doc)

    html = HTML5_TEMPLATE.substitute(title=title, body=body)
    print(html)


if __name__ == "__main__":
    main(sys.argv[1:])
