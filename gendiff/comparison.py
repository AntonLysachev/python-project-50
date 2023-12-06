def get_diff(data1, data2):
    diff = {}
    all_keys = data1.keys() | data2.keys()
    removed_keys = data1.keys() - data2.keys()
    added_keys = data2.keys() - data1.keys()
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        diff.update({key: {}})
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key].update({'type': 'nested', 'children':
                              get_diff(data1[key], data2[key])})
            continue
        if key in removed_keys:
            diff[key].update({'type': 'removed', 'value': value1})
            continue
        if key in added_keys:
            diff[key].update({'type': 'added', 'value': value2})
            continue
        if value1 == value2:
            diff[key].update({'type': 'not updated',
                              'value': value1})
            continue
        diff[key].update({'type': 'updated',
                          'old_value': value1,
                          'new_value': value2})
    return dict(sorted(diff.items()))
