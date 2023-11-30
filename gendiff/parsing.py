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


def add_data(data1, data2, key):
    only_one = data1.keys() - data2.keys()
    only_tow = data2.keys() - data1.keys()
    common = data2.keys() & data1.keys()
    value1 = data1.get(key)
    value2 = data2.get(key)
    if key in only_one:
        return {'type': 'removed', 'value': add_nest(value1)}
    if key in only_tow:
        return {'type': 'added', 'value': add_nest(value2)}
    if key in common:
        if value1 == value2:
            return {'type': 'not updated', 'value': add_nest(value1)}
        else:
            return {'type': 'updated',
                    'old_value': add_nest(value1),
                    'new_value': add_nest(value2)}


def analyze(data1, data2):
    analyzed = {}
    all_keys = data1.keys() | data2.keys()
    for key in all_keys:
        analyzed.update({key: {}})
        if isinstance(data1.get(key), dict):
            if isinstance(data2.get(key), dict):
                analyzed[key].update({'children':
                                      analyze(data1[key], data2[key])})
                continue
        analyzed[key].update(add_data(data1, data2, key))
    return dict(sorted(analyzed.items()))
