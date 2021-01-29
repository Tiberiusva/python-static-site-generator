import sys
from pathlib import Path


class Site:

    def __init__(self, source, destination, parsers=None):
        self.source = Path(source)
        self.destination = Path(destination)
        self.parsers = parsers or []

    def create_dir(self, path):
        directory = self.destination / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.destination.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)

    def load_parser(self, extension):
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser

    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        if parser is not None:
            parser.parse(path, self.source, self.destination)
        else:
            self.error("No parser for the {} extension, file skipped!".format(path.suffix))

    @staticmethod
    def error(message):
        sys.stderr.write("\x1b[1;31m{}\n".format(message))
