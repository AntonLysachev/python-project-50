def to_str(value, depth):
    if isinstance(value, dict):
        lines = ['{']
        indent = ' ' * depth
        bottom_indent = ' ' * (depth - 2)
        for key, value in value.items():
            line = f'{indent}  {key}: {to_str(value, depth + 4)}'
            lines.append(line)
        lines.append(f'{bottom_indent}{"}"}')
        return '\n'.join(flatten(lines))
    if isinstance(value, bool):
        match value:
            case False:
                return 'false'
            case True:
                return 'true'
    if value is None:
        return 'null'
    return value


def flatten(tree):
    result = []
    for item in tree:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def build_line(key, value, depth):
    indent = ' ' * (depth - 4)
    lines = []
    current_type = value['type']
    value_in = value.get('value')
    match current_type:
        case 'nested':
            bottom_indent = ' ' * (depth - 2)
            child = value["children"]
            lines.append(f'{indent}  {key}: {"{"}')
            for key, value in child.items():
                lines.append(f'{build_line(key, value, depth + 4)}')
            lines.append(f'{bottom_indent}{"}"}')
            return '\n'.join(lines)
        case 'updated':
            old = value["old_value"]
            new = value["new_value"]
            lines.append(f'{indent}- {key}: {to_str(old, depth)}')
            lines.append(f'{indent}+ {key}: {to_str(new, depth)}')
            return '\n'.join(lines)
        case 'not updated':
            return f'{indent}  {key}: {value_in}'
        case 'removed':
            return f'{indent}- {key}: {to_str(value_in, depth)}'
        case 'added':
            return f'{indent}+ {key}: {to_str(value_in, depth)}'


def form_tree(dict_diff, depth=2):
    lines = ['{']
    bottom_indent = ' ' * (depth - 2)
    for key, value in dict_diff.items():
        lines.append(build_line(key, value, depth + 4))
    lines.append(f'{bottom_indent}{"}"}')
    return '\n'.join(flatten(lines))
