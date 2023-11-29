def complex_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value in ['null', 'false', 'true', 'empty']:
        return value
    if isinstance(value, int):
        return value
    return f"'{value}'"


def print_volue(path, value):
    old_value = complex_value(value.get('old_value'))
    new_value = complex_value(value.get('new_value'))
    value_in = complex_value(value.get('value'))
    type_value = value['type']
    print_path = '.'.join(path)
    if type_value == 'added':
        return f"'{print_path}' was added with value: {value_in}"
    if type_value == 'removed':
        return f"'{print_path}' was removed"
    if type_value == 'updated':
        return f"'{print_path}' was updated. From {old_value} to {new_value}"


def plain(parsing_file, path=[]):
    report = []
    for key, value in parsing_file.items():
        path.append(key)
        if value.get('children'):
            report.append(plain(value["children"], path))
        else:
            print = print_volue(path, value)
            if print is not None:
                report.append(f'Property {print}')
        path.pop()
    return report
