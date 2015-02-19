import itertools
#import reprlib
import inspect

def full_sig(method):
    try:
        return method.__name__ + inspect.signature(method)
    except ValueError:
        return method.__name__ + '(...)'

def brief_doc(obj):
    doc = obj.__doc__
    if doc is not None:
        lines = doc.splitlines()
        if len(lines) > 0:
            return lines[0]
    return ''

def print_table(row_of_columns, *headers):
    num_columns = len(row_of_columns[0])
    num_headers = len(headers)
    if num_headers != num_columns:
        raise TypeError("Expected {} header arguments,"
                        "get {}".format(num_headers, num_columns))
    rows_of_columns_with_header = itertools.chain([headers], row_of_columns)
    columns_of_rows = list(zip(*rows_of_columns_with_header))
    column_width = [max(map(len, colmun)) for colmun in columns_of_rows]
    # {:13} this will format the column with width
    # use {{}} to excape the outer cule brace
    column_specs = ('{{:{w}}}'.format(w=width) for width in column_width)
    # generate format_spec
    format_spec = ' '.join(column_specs)

    print(format_spec.format(*headers))
    rules = ('-' * width for width in column_width)
    print(format_spec.format(*rules))
    for row in row_of_columns:
        print(format_spec.format(*row))

def dump(obj):
    print("Type")
    print("=====")
    print(type(obj))
    print()

    print("document")
    print("===========")
    print(inspect.getdoc(obj))
    print()

    print("Attributes")
    print("=============")
    all_attrs = set(dir(obj))
    method_names= set(filter(lambda attr_name: callable(getattr(obj, attr_name)), all_attrs))
    assert method_names <= all_attrs
    attr_names = all_attrs - method_names
    attr_names_and_values = [(name, repr(getattr(obj, name))) for name in attr_names]
    print_table(attr_names_and_values, "Name", "Value")
    print()

    print("Methods")
    print("==============")
    methods = (getattr(obj, method_name) for method_name in method_names)
    method_names_and_doc = [(full_sig(method), brief_doc(method))
                            for method in methods]
    print_table(method_names_and_doc, "Name", "Desc")

    print()




