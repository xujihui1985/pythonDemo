def hypervolumne(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v

def tag(name, **kwargs):
    result = '<' + name
    for key, value in kwargs.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result



