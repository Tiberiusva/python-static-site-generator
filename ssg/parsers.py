from typing import List
from pathlib import Path
import shutil

class Parser:
    
    extensions:List[str]=[]
    def valid_extension(self,extension):
        return extension in self.extensions

    def parse(path:Path,source:Path,dest:Path):
        raise NotImplementedError()

    def read(self,path):
        with open(path,"r") as f:
            return f.read()

    def write(path,dest,content,ext=".html"):
        full_path= dest / path.with_suffix(ext).name
        with open(fullpath,"w") as file:
            file.write(content)

    def copy(path, source, dest):
        shutil.copy2(path,dest / path.relative_to(source))

class ResourceParser(Parser):
    extensions = [".jpg",".png",".gif",".css",".html"]

    def parse(self,path,source,dest):
        self.copy(path,source,dest)

    
