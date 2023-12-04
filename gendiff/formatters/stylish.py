def to_json_style(value):  # не понимаю как тут использовать isinstance
    match value:
        case None:
            return 'null'
        case False:
            return 'false'
        case True:
            return 'true'
        case _:
            return value


# функция add_nest не переводит в строку, а создает древовидую структуру
# не понимаю зачем их объеденять они занимаются разным
def form_nest(value, space, deep, report=''):
    space = '  ' * deep
    down_space = '  ' * (deep - 2)
    if isinstance(value, dict):
        for key, value in value.items():
            value_in = to_json_style(value)
            report = f'{report}{space}{key}: '
            report = f'{report}{form_nest(value_in, space, deep + 2)}\n'
        return f'{{\n{report}{down_space}}}'
    return value


def form_value(key, value, space, deep):
    type_value = value['type']
    if type_value == 'updated':
        old = to_json_style(value["old_value"])
        new = to_json_style(value["new_value"])
        report = f'{space}- {key}: {form_nest(old, space, deep)}\n'
        report = f'{report}{space}+ {key}: {form_nest(new, space, deep)}\n'
        return report
    value_in = to_json_style(value['value'])
    if type_value == 'not updated':
        return f'{space}  {key}: {value_in}\n'
    if type_value == 'removed':
        return f'{space}- {key}: {form_nest(value_in, space, deep)}\n'
    if type_value == 'added':
        return f'{space}+ {key}: {form_nest(value_in, space, deep)}\n'


def form_tree(parsing_file, deep=1, report=''):
    space = '  ' * deep
    down_space = '  ' * (deep - 1)
    for key, value in parsing_file.items():
        type_value = value['type']
        if type_value == 'nested':
            report = f'{report}{space}  {key}:'
            report = f'{report} {form_tree(value["children"], deep + 2)}\n'
        else:
            report = f'{report}{form_value(key, value, space, deep + 3)}'
    return f'{{\n{report}{down_space}}}'
