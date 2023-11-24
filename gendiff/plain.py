def complex_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value in ['null', 'false', 'true', 'empty']:
        return value
    if isinstance(value, int):
        return value
    return f"'{value}'"


def print_volue(path, value):
    value1 = complex_value(value['value1'])
    value2 = complex_value(value['value2'])
    print_path = '.'.join(path)
    if value1 == 'empty':
        return f"'{print_path}' was added with value: {value2}"
    if value2 == 'empty':
        return f"'{print_path}' was removed"
    if value1 != value2 and value1 != 'empty' and value2 != 'empty':
        return f"'{print_path}' was updated. From {value1} to {value2}"


def plain(parsing_file, path=[], out=''):
    for key, value in parsing_file.items():
        path.append(key)
        if value.get('children'):
            out = f'{out}{plain(value["children"], path)}'
        else:
            print = print_volue(path, value)
            if print is not None:
                out = f'{out}Property {print}\n'
        path.pop()
    return out
