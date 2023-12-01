def write_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    match value:
        case None:
            return 'null'
        case False:
            return 'false'
        case True:
            return 'true'
        case _:
            if isinstance(value, int):
                return value
            return f"'{value}'"


def flatten(tree):
    result = []

    def walk(subtree):
        for item in subtree:
            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)
    walk(tree)
    return result


def print_volue(path, value):
    old_value = write_value(value.get('old_value'))
    new_value = write_value(value.get('new_value'))
    value_to_write = write_value(value.get('value'))
    type_value = value['type']
    print_path = '.'.join(path)
    if type_value == 'added':
        return f"'{print_path}' was added with value: {value_to_write}"
    if type_value == 'removed':
        return f"'{print_path}' was removed"
    if type_value == 'updated':
        return f"'{print_path}' was updated. From {old_value} to {new_value}"


def form_plain(parsing_file):
    def form(parsing_file, path=[]):
        report = []
        for key, value in parsing_file.items():
            path.append(key)
            if value.get('children'):
                report.append(form(value["children"], path))
            else:
                print = print_volue(path, value)
                if print is not None:
                    report.append(f'Property {print}')
            path.pop()
        return report
    return '\n'.join(flatten(form(parsing_file)))
