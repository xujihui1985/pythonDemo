def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls


