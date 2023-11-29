def nest(node, space, deep, report=''):
    space = '  ' * deep
    down_space = '  ' * (deep - 2)
    if isinstance(node, dict):
        for key, value in node.items():
            report = f'{report}{space}{key}: '
            report = f'{report}{nest(value["value"], space, deep + 2)}\n'
        return f'{{\n{report}{down_space}}}'
    return node


def print_value(key, value, space, deep):
    type_value = value['type']
    if type_value == 'not updated':
        return f'{space}  {key}: {value["value"]}\n'
    if type_value == 'removed':
        return f'{space}- {key}: {nest(value["value"], space, deep)}\n'
    if type_value == 'added':
        return f'{space}+ {key}: {nest(value["value"], space, deep)}\n'
    if type_value == 'updated':
        old_value = value["old_value"]
        new_value = value["new_value"]
        report = f'{space}- {key}: {nest(old_value, space, deep)}\n'
        report = f'{report}{space}+ {key}: {nest(new_value, space, deep)}\n'
        return report


def stylish(parsing_file, deep=1, report=''):
    space = '  ' * deep
    down_space = '  ' * (deep - 1)
    for key, value in parsing_file.items():
        if value.get('children'):
            report = f'{report}{space}  {key}:'
            report = f'{report} {stylish(value["children"], deep + 2)}\n'
        else:
            report = f'{report}{print_value(key, value, space, deep + 3)}'
    return f'{{\n{report}{down_space}}}'
