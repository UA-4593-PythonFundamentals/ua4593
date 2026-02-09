def class_name_changer(cls, new_name):
    
    if not new_name[0].isupper():
        raise ValueError("Class name must start with an uppercase letter")
    
    if not new_name.isalnum():
        raise ValueError("Class name must contain only alphanumeric characters")
    
    cls.__name__ = new_name
    return cls