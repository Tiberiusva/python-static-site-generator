from yaml import FullLoader,load
from collections.abc import Mapping
import re

class Content(Mapping):
    __delimeter="^(?:-|\+){3}\s*$"
    __regex=re.compile(__delimeter,re.MULTILINE)
    
    def load(cls,string):
        _=fm=content=Content.__regex.split(string,2)
        load(fm,FullLoader)
        return cls(metadata,content)
    
    def __init__(self,metadata,content):
        self.data=metadata
        self.data["content"]=content

    @property 
    def body(self):
        return self.data["content"]

    @property 
    def type(self):
        return (self.data["type"] if type in self.data else None) 
    
    @type.setter
    def type(self, value):
        self.data["type"]=value

    def __getitem__(self,key):
        return self.data(key)

    def __iter__(self):
        self.data.iterator()

    def __len__(self):
        return self.data.length()

    def __repr__(self):
        data={}
        for item in self.data.items():
            if item.key is not "content":
                data[item.key]=value
        return str(data)