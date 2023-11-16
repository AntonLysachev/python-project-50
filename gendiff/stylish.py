def print_dict(node, space, deep, out=''):
    space = '  ' * deep
    down_space = '  ' * (deep - 2)
    for key, value in node.items():
        if isinstance(value, dict):
            out = f'{out}{space}{key}: '
            out = f'{out}{print_dict(value, space, deep + 2)}\n'
        else:
            out = f'{out}{space}{key}: {value}\n'
    return f'{{\n{out}{down_space}}}'


def print_value(key, value, space, deep):
    value1 = value['value1']
    value2 = value['value2']
    if value1 == value2:
        return f'{space}  {key}: {value1}\n'
    if value2 == 'empty':
        if isinstance(value1, dict):
            return f'{space}- {key}: {print_dict(value1, space, deep)}\n'
        return f'{space}- {key}: {value1}\n'
    if value1 == 'empty':
        if isinstance(value2, dict):
            return f'{space}+ {key}: {print_dict(value2, space, deep)}\n'
        return f'{space}+ {key}: {value2}\n'
    if isinstance(value1, dict):
        out = f'{space}- {key}: '
        out = f'{out}{print_dict(value1, space, deep)}\n'
        out = f'{out}{space}+ {key}: {value2}\n'
        return out
    if isinstance(value2, dict):
        out = f'{space}+ {key}: '
        out = f'{out}{print_dict(value2, space, deep)}\n'
        out = f'{out}{space}- {key}: {value2}\n'
        return out
    return f'{space}- {key}: {value1} \n{space}+ {key}: {value2}\n'


def stylish(parsing_file):
    def styler(parsing_file, deep=1, out=''):
        space = '  ' * deep
        down_space = '  ' * (deep - 1)
        for key, value in parsing_file.items():
            if value.get('children'):
                out = f'{out}{space}  {key}:'
                out = f'{out} {styler(value["children"], deep + 2)}\n'
                continue
            out = f'{out}{print_value(key, value, space, deep + 3)}'
        return f'{{\n{out}{down_space}}}'
    out = styler(parsing_file)
    return out
