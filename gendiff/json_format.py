def added(value):
    added_key = {}
    added_key.update({'type': 'added'})
    added_key.update({'value': value})
    return added_key


def updated(old_value, new_value):
    updated_key = {}
    updated_key.update({'type': 'updated'})
    updated_key.update({'old_value': old_value})
    updated_key.update({'new_value': new_value})
    return updated_key


def removed(value):
    removed_key = {}
    removed_key.update({'type': 'removed'})
    removed_key.update({'value': value})
    return removed_key


def not_updated(value):
    not_updated_key = {}
    not_updated_key.update({'type': 'not updated'})
    not_updated_key.update({'value': value})
    return not_updated_key


def nested(value):
    nested_key = {}
    if isinstance(value, dict):
        for key, value_in in value.items():
            nested_key.update({key: {}})
            nested_key[key].update({'type': 'nested'})
            if isinstance(value_in, dict):
                nested_key[key].update({'value': nested(value_in)})
            else:
                nested_key[key].update({'value': value_in})
        return nested_key
    return value


def print_value(value):
    value1 = nested(value['value1'])
    value2 = nested(value['value2'])
    if value1 == 'empty':
        return added(value2)
    if value2 == 'empty':
        return removed(value1)
    if value1 != value2 and value1 != 'empty' and value2 != 'empty':
        return updated(value1, value2)
    return not_updated(value1)


def json_format(parsing_file):
    json_file = {}
    for key, value in parsing_file.items():
        json_file.update({key: {}})
        if value.get('children'):
            json_file[key].update({'children': json_format(value['children'])})
        else:
            json_file[key].update(print_value(value))
    return json_file
