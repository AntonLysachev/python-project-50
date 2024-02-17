from gendiff.file_reader import get_data
from gendiff.formatters.applicator import apply_format


def build_diff_tree(data1, data2):
    diff = {}
    all_keys = data1.keys() | data2.keys()
    removed_keys = data1.keys() - data2.keys()
    added_keys = data2.keys() - data1.keys()
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        # diff.update({key: {}})
        diff[key] = {}
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key].update({'type': 'nested', 'children':
                              build_diff_tree(value1, value2)})
        elif key in removed_keys:
            diff[key].update({'type': 'removed', 'value': value1})  
        elif key in added_keys:
            diff[key].update({'type': 'added', 'value': value2})
        elif value1 == value2:
            diff[key].update({'type': 'not updated',
                              'value': value1})
        else:
            diff[key].update({'type': 'updated',
                            'old_value': value1,
                            'new_value': value2})
    return dict(sorted(diff.items()))


def generate_diff(file1, file2, format_name='stylish'):
    data1 = get_data(file1)
    data2 = get_data(file2)
    dict_diff = build_diff_tree(data1, data2)
    return apply_format(format_name, dict_diff)
