def nest(node, space, deep, out=''):
    space = '  ' * deep
    down_space = '  ' * (deep - 2)
    if isinstance(node, dict):
        for key, value in node.items():
            out = f'{out}{space}{key}: '
            out = f'{out}{nest(value["value"], space, deep + 2)}\n'
        return f'{{\n{out}{down_space}}}'
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
        out = f'{space}- {key}: {nest(value["old_value"], space, deep)}\n'
        out = f'{out}{space}+ {key}: {nest(value["new_value"], space, deep)}\n'
        return out


def stylish(parsing_file, deep=1, out=''):
    space = '  ' * deep
    down_space = '  ' * (deep - 1)
    for key, value in parsing_file.items():
        if value.get('children'):
            out = f'{out}{space}  {key}:'
            out = f'{out} {stylish(value["children"], deep + 2)}\n'
        else:
            out = f'{out}{print_value(key, value, space, deep + 3)}'
    return f'{{\n{out}{down_space}}}'
