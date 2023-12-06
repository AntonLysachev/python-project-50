def to_str(value):
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
    old_value = to_str(value.get('old_value'))
    new_value = to_str(value.get('new_value'))
    value_to_write = to_str(value.get('value'))
    current_type = value['type']
    print_path = '.'.join(path)
    if current_type == 'added':
        return f"'{print_path}' was added with value: {value_to_write}"
    if current_type == 'removed':
        return f"'{print_path}' was removed"
    if current_type == 'updated':
        return f"'{print_path}' was updated. From {old_value} to {new_value}"


def form_plain(dict_diff):
    def form(dict_diff, path=[]):
        report = []
        for key, value in dict_diff.items():
            path.append(key)
            if value.get('children'):
                report.append(form(value["children"], path))
            else:
                print = print_volue(path, value)
                if print is not None:
                    report.append(f'Property {print}')
            path.pop()
        return report
    return '\n'.join(flatten(form(dict_diff)))
