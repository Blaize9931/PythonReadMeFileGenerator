import textwrap

def markdown(results):
    title= results["title"]
    description= results["description"]
    installation=results["installation"]
    usage=results["usage"]
    license=results["license"]
    author=results["author"]
    contact=results["contact"]
    return textwrap.dedent(f"""\\
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