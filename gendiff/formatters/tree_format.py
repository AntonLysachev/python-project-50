from gendiff.formatters.json_styler import to_json_style


def add_nest(node, space, deep, report=''):
    space = '  ' * deep
    down_space = '  ' * (deep - 2)
    if isinstance(node, dict):
        for key, value in node.items():
            value_in = to_json_style(value['value'])
            report = f'{report}{space}{key}: '
            report = f'{report}{add_nest(value_in, space, deep + 2)}\n'
        return f'{{\n{report}{down_space}}}'
    return node


def print_value(key, value, space, deep):
    type_value = value['type']
    if type_value == 'updated':
        old_value = to_json_style(value["old_value"])
        new_value = to_json_style(value["new_value"])
        report = f'{space}- {key}: {add_nest(old_value, space, deep)}\n'
        report = f'{report}{space}+ {key}: {add_nest(new_value, space, deep)}\n'
        return report
    value_in = to_json_style(value['value'])
    if type_value == 'not updated':
        return f'{space}  {key}: {value_in}\n'
    if type_value == 'removed':
        return f'{space}- {key}: {add_nest(value_in, space, deep)}\n'
    if type_value == 'added':
        return f'{space}+ {key}: {add_nest(value_in, space, deep)}\n'


def print_tree(parsing_file, deep=1, report=''):
    space = '  ' * deep
    down_space = '  ' * (deep - 1)
    for key, value in parsing_file.items():
        if value.get('children'):
            report = f'{report}{space}  {key}:'
            report = f'{report} {print_tree(value["children"], deep + 2)}\n'
        else:
            report = f'{report}{print_value(key, value, space, deep + 3)}'
    return f'{{\n{report}{down_space}}}'
