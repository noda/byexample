# Generate an index for all examples

import datetime
import os
import pathlib
import sys
from string import Template

import frontmatter
import yaml
from marko import Markdown
from marko.block import Heading

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
                title = extract_title_from_md_file(file_path)

                output[dirpath]["examples"].append(
                    {
                        "path": pathlib.Path(*p.parts[1:])
                        .as_posix()
                        .replace(".md", ".html"),
                        "title": title,
                        "frontmatter": frontmatter.load(file_path).metadata,
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

    # sort by product name
    structure = {
        k: v
        for k, v in sorted(
            structure.items(), key=lambda item: item[1]["metadata"]["product"]
        )
    }

    # sort examples by frontmatter priority and title
    structure = {
        k: {
            "metadata": v["metadata"],
            "examples": sorted(
                v["examples"],
                key=lambda item: (
                    item["frontmatter"].get("priority", 9999),
                    item["title"],
                ),
            ),
        }
        for k, v in structure.items()
    }

    md_content = render_structure_as_md(structure)

    title = "NODA by Example"

    md = Markdown()
    content = MD_TEMPLATE.substitute(title=title, body=md_content)

    doc = md.parse(content)
    body = md.renderer.render(doc)

    with open("templates/index.html", "r") as f:
        template = Template(f.read())

    # Current date on the format March 15, 2023
    todate = datetime.datetime.now().strftime("%B %d, %Y")

    html = template.substitute(
        title=title,
        description="If you're an engineer or researcher looking to interact with our systems, NODA by Example is the perfect place to start. This hands-on introduction will guide you through our platform and provide you with the knowledge and skills you need to make the most of our solutions. Get ready to take control of your energy resources and experience the power of NODA.",
        body=body,
        last_updated=todate,
    )
    print(html)


if __name__ == "__main__":
    main(sys.argv[1:])
