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
# def print_dict(node, space, deep, out=''):
#     space = '  ' * deep
#     down_space = '  ' * (deep - 2)
#     for key, value in node.items():
#         if isinstance(value, dict):
#             out = f'{out}{space}{key}: '
#             out = f'{out}{print_dict(value, space, deep + 2)}\n'
#         else:
#             out = f'{out}{space}{key}: {value}\n'
#     return f'{{\n{out}{down_space}}}'


# def print_value(key, value, space, deep):
#     value1 = value['value1']
#     value2 = value['value2']
#     out = ''
#     if value1 == value2:
#         return f'{space}  {key}: {value1}\n'
#     if value1 != value2 and value1 != 'empty':
#         if isinstance(value1, dict):
#             out = f'{space}- {key}: {print_dict(value1, space, deep)}\n'
#         else:
#             out = f'{space}- {key}: {value1}\n'
#     if value2 != 'empty':
#         if isinstance(value2, dict):
#             out = f'{out}{space}+ {key}: {print_dict(value2, space, deep)}\n'
#         else:
#             out = f'{out}{space}+ {key}: {value2}\n'
#     return out


# def stylish(parsing_file, deep=1, out=''):
#     space = '  ' * deep
#     down_space = '  ' * (deep - 1)
#     for key, value in parsing_file.items():
#         if value.get('children'):
#             out = f'{out}{space}  {key}:'
#             out = f'{out} {stylish(value["children"], deep + 2)}\n'
#         else:
#             out = f'{out}{print_value(key, value, space, deep + 3)}'
#     return f'{{\n{out}{down_space}}}'
