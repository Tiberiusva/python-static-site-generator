import typer
from ssg.site import Site
import ssg.parsers


def main(source="content", dest="dist"):
    parsers = [ssg.parsers.ResourceParser(), ssg.parsers.MarkdownParser(), ssg.parsers.ReStructuredTextParser()]
    for p in parsers:
        print(p.__repr__)
    config = {'source': source, 'destination': dest, 'parsers': parsers}
    Site(**config).build()


typer.run(main)