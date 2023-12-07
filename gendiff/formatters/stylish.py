def to_str(value, deep):
    lines = ['{']
    space = ' ' * deep
    down_space = ' ' * (deep - 2)
    if isinstance(value, dict):
        for key, value in value.items():
            line = f'{space}  {key}: {to_str(value, deep + 4)}'
            lines.append(line)
        lines.append(f'{down_space}{"}"}')
        return '\n'.join(flatten(lines))
    # Не понимаю как тут сделать проверку через isinstance
    match value:
        case None:
            return 'null'
        case False:
            return 'false'
        case True:
            return 'true'
        case _:
            return value


def flatten(tree):
    result = []
    for item in tree:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def build_line(key, value, deep):
    space = ' ' * (deep - 4)
    lines = []
    current_type = value['type']
    value_in = value.get('value')
    match current_type:
        case 'nested':
            down_space = ' ' * (deep - 2)
            child = value["children"]
            lines.append(f'{space}  {key}: {"{"}')
            for key, value in child.items():
                lines.append(f'{build_line(key, value, deep + 4)}')
            lines.append(f'{down_space}{"}"}')
            return '\n'.join(lines)
        case 'updated':
            old = value["old_value"]
            new = value["new_value"]
            lines.append(f'{space}- {key}: {to_str(old, deep)}')
            lines.append(f'{space}+ {key}: {to_str(new, deep)}')
            return '\n'.join(lines)
        case 'not updated':
            return f'{space}  {key}: {value_in}'
        case 'removed':
            return f'{space}- {key}: {to_str(value_in, deep)}'
        case 'added':
            return f'{space}+ {key}: {to_str(value_in, deep)}'


def form_tree(dict_diff, deep=2):
    lines = ['{']
    down_space = ' ' * (deep - 2)
    for key, value in dict_diff.items():
        lines.append(build_line(key, value, deep + 4))
    lines.append(f'{down_space}{"}"}')
    return '\n'.join(flatten(lines))
