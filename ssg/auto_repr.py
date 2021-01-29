import inspect

def auto_repr(cls):
    #print(f"Decorating {cls.__name__} with auto_repr")
    members=vars(cls)
    #for name,member in members.items():
    #    print(name,member)
    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines a __repr__")
    if "__init__" in members:
        raise TypeError(f"{cls.__name__} does not override __init__")

    sig=inspect.signature(cls.__init__)
    parameter_names=list(sig.parameters)[1:]
    #print("__init__ parameter names:",parameter_names)
    if not all(
        isinstance(members.get(name,None),property)
        for name in parameter_names
    ):
        return cls
        #raise TypeError(
        #    f"Cannot apply auto_repr to {cls.__name__} because not all "
       #     " __init__ parameters have matching properties"
        #)

    def synthesized_repr(self):
        return "{typename}({args})".format(
            typename=typename(self),
            args=", ".join(
                "{name}={value!r}".format(
                    name=name,value=getattr(self,name)
                )for name in parameter_names
            )
        )
    setattr(cls,"__repr__",synthesized_repr)
    return cls



