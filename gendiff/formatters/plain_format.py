def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        match value:
            case False:
                return 'false'
            case True:
                return 'true'
    if isinstance(value, int):
        return value
    if value is None:
        return 'null'
    return f"'{value}'"


def flatten(tree):
    result = []
    for item in tree:
        if item is None:
            continue
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def build_line(print_path, value):
    current_type = value['type']
    match current_type:
        case 'added':
            line = to_str(value.get('value'))
            return f"Property '{print_path}' was added with value: {line}"
        case 'removed':
            return f"Property '{print_path}' was removed"
        case 'updated':
            old = to_str(value.get('old_value'))
            new = to_str(value.get('new_value'))
            return f"Property '{print_path}' was updated. From {old} to {new}"
        case 'nested':
            child = value["children"]
            lines = []
            for key, value in child.items():
                lines.append(build_line(f"{print_path}.{key}", value))
            return '\n'.join(flatten(lines))


def form_plain(dict_diff):
    lines = []
    path = []
    for key, value in dict_diff.items():
        path.append(key)
        print_path = '.'.join(path)
        lines.append(build_line(print_path, value))
        path.pop()
    return '\n'.join(flatten(lines))
