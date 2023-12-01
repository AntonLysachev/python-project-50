def add_nest(value):
    nested_key = {}
    if isinstance(value, dict):
        for key, value_in in value.items():
            nested_key.update({key: {}})
            nested_key[key].update({'type': 'nested'})
            if isinstance(value_in, dict):
                nested_key[key].update({'value': add_nest(value_in)})
            else:
                nested_key[key].update({'value': value_in})
        return nested_key
    return value


# Несовсем понял праку насчет nested. У меня же есть add_nest
# Или имеется ввиду что каждое вложение надо пометить nested
# Я думал children достаточно
def analyze(data1, data2):
    analyzed = {}
    all_keys = data1.keys() | data2.keys()
    removed_keys = data1.keys() - data2.keys()
    added_keys = data2.keys() - data1.keys()
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        analyzed.update({key: {}})
        if isinstance(value1, dict) and isinstance(value2, dict):
            analyzed[key].update({'children':
                                  analyze(data1[key], data2[key])})
            continue
        if key in removed_keys:
            analyzed[key].update({'type': 'removed', 'value': add_nest(value1)})
            continue
        if key in added_keys:
            analyzed[key].update({'type': 'added', 'value': add_nest(value2)})
            continue
        if value1 == value2:
            analyzed[key].update({'type': 'not updated',
                                  'value': add_nest(value1)})
            continue
        analyzed[key].update({'type': 'updated',
                              'old_value': add_nest(value1),
                              'new_value': add_nest(value2)})
    return dict(sorted(analyzed.items()))
