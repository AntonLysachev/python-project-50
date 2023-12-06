def to_str(value, space, deep):
    lines = ['{']
    space = '  ' * deep
    down_space = '  ' * (deep - 2)
    if isinstance(value, dict):
        for key, value in value.items():
            line = f'{space}{key}: {to_str(value, space, deep + 2)}'
            lines.append(line)
        lines.append(f'{down_space}{"}"}')
        return '\n'.join(flatten(lines))
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

    def walk(subtree):
        for item in subtree:
            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)
    walk(tree)
    return result


def build_line(key, value, space, deep):
    lines = []
    current_type = value['type']
    if current_type == 'updated':
        old_value = value["old_value"]
        new_value = value["new_value"]
        lines.append(f'{space}- {key}: {to_str(old_value, space, deep)}')
        lines.append(f'{space}+ {key}: {to_str(new_value, space, deep)}')
        return lines
    value_in = value['value']
    if current_type == 'not updated':
        return f'{space}  {key}: {value_in}'
    if current_type == 'removed':
        return f'{space}- {key}: {to_str(value_in, space, deep)}'
    if current_type == 'added':
        return f'{space}+ {key}: {to_str(value_in, space, deep)}'


def form_tree(parsing_file, deep=1):
    lines = ['{']
    space = '  ' * deep
    down_space = '  ' * (deep - 1)
    for key, value in parsing_file.items():
        current_type = value['type']
        if current_type == 'nested':
            child = value["children"]
            lines.append(f'{space}  {key}: {form_tree(child, deep + 2)}')
        else:
            lines.append(build_line(key, value, space, deep + 3))
    lines.append(f'{down_space}{"}"}')
    return '\n'.join(flatten(lines))
