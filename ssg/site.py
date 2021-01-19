from pathlib import path 
import os
class Site:
    def __init__(self,source,dest):
        self.source=Ppath.ath(source)
        self.dest=path.Path(dest)

    def create_dir(self,path):
        directory = self.dest +"/"+ path.relative_to(self.source)
        diretory.mkdir(parents=True,exist_ok=True)
    
    def build(self):
         self.dest.mkdir(parents=True,exist_ok=True)
         for path in self.source.rglob("*")
            if os.path.isdir(path)
                create_dir(path)