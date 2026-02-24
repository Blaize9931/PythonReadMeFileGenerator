import textwrap

def markdown(results):
    title= results["title"]
    description= results["description"]
    installation=results["installation"]
    usage=results["usage"]
    license=results["license"]
    author=results["author"]
    contact=results["contact"]
    content = textwrap.dedent(f"""\
# {title}

## Description
{description}

## Installation
{installation}

## Usage
{usage}

## License
{license}

## Author
{author}

## Contact Details
{contact}
""")
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(content)