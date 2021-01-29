import sys
from docutils.core import publish_parts
from markdown import markdown
from ssg.content import Content
from typing import List
from pathlib import Path
import shutil
from ssg.auto_repr import *


@auto_repr
class Parser:
    
    extensions:List[str]=[]
    def valid_extension(self,extension):
        return extension in self.extensions

    def parse(self,path:Path,source:Path,dest:Path):
        raise NotImplementedError

    @property
    def path(self):
        return self.path
    @property
    def source(self):
        return self.source
    @property
    def dest(self):
        return self.dest

    def read(self,path):
        with open(path,"r") as file:
            return file.read()
    def write(self,path,dest,content,ext=".html"):
        full_path= dest / path.with_suffix(ext).name
        with open(full_path,"w") as file:
            file.write(content)

    def copy(self,path, source, dest):
        shutil.copy2(path,dest / path.relative_to(source))
    

@auto_repr
class ResourceParser(Parser):
    extensions = [".jpg",".png",".gif",".css",".html"]
    def parse(self,path,source,dest):
        self.copy(path,source,dest)

@auto_repr
class MarkdownParser(Parser):
    extensions:List[str]=[".md",".markdown"]

    def parse(self,path:Path,source:Path,dest:Path):
        content=Content.load(self.read(path))
        html = markdown(content.body)
        self.write(path,dest,html)
        sys.stdout.write("\x1b[1;32m{} converted to HTML. Metadata: {}\n".format( path.name, content))

@auto_repr   
class ReStructuredTextParser(Parser):
    extensions:List[str]=[".rst"]
    def parse(self,path:Path,source:Path,dest:Path):
        content=Content.load(self.read(path))
        html=publish_parts(content.body,writer_name="html5")
        self.write(path,dest,html["html_body"])
        sys.stdout.write("\x1b[1;32m{} converted to HTML. Metadata: {}\n".format(path.name,content))