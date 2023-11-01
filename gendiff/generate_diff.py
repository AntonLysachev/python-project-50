import json
import copy


def get_data(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data


def ref_keys(data1, data2):
    merg_data = {}
    merg_data.update(data1)
    merg_data.update(data2)

    def for_ref(data, ref={}):
        copy_data = copy.deepcopy(data)
        for key, value in copy_data.items():
            ref.update({key: None})
            if isinstance(value, dict):
                ref.update({key: value})
                ref[key].update(for_ref(value, ref={}))
        return ref
    return dict(sorted(merg_data.items()))


def format(ref_file, file, merg_keys, tab='', out=''):
    for key, value in merg_keys.items():
        if key in ref_file:
            if key in file:
                if isinstance(value, dict):
                    out = f"{out}   {key}: "
                    tab_in = f'{tab}{" "*len(out)}'
                    deep_data = format(ref_file.get(key, {}),
                                       file.get(key, {}), value, tab_in, out='')
                    out = f"{out}{deep_data}\n"
                else:
                    if ref_file[key] == file[key]:
                        out = f'{out} {tab}  {key}: {ref_file[key]}\n'
                    else:
                        out = f'{out}{tab} - {key}: {ref_file[key]}\n'
                        out = f'{out}{tab} + {key}: {file[key]}\n'
            else:
                out = f'{out}{tab} - {key}: {ref_file[key]}\n'
        else:
            out = f'{out}{tab} + {key}: {file[key]}\n'
    return f'{{\n{out}{tab}}}'


def generate_diff(file1, file2):
    data_file1 = get_data(file1)
    data_file2 = get_data(file2)
    merg_keys = ref_keys(data_file1, data_file2)
    out = format(data_file1, data_file2, merg_keys)
    return out
