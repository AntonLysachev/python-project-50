import json


def get_data(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data


def parsing_files(data1, data2):
    data = {}
    only_one = data1.keys() - data2.keys()
    only_tow = data2.keys() - data1.keys()
    common = data1.keys() & data2.keys()
    for key in only_one:
        data.update({key: {'prefix': '-'}})
        data[key].update({'name': key})
        data[key].update({'data':  data1[key]})
    for key in only_tow:
        data.update({key: {'prefix': '+'}})
        data[key].update({'name': key})
        data[key].update({'data':  data2[key]})
    for key in common:
        if data1[key] == data2[key]:
            data.update({key: {'prefix': ' '}})
            data[key].update({'name': key})
            data[key].update({'data':  data1[key]})
        else:
            data.update({f'{key}1': {'prefix': '-'}})
            data[f'{key}1'].update({'name': key})
            data[f'{key}1'].update({'data':  data1[key]})
            data.update({f'{key}2': {'prefix': '+'}})
            data[f'{key}2'].update({'name': key})
            data[f'{key}2'].update({'data':  data2[key]})
    return dict(sorted(data.items()))


def format(compare_data):
    out = ''
    for value in compare_data.values():
        out = f'{out} {value["prefix"]} {value["name"]}: {value["data"]}\n'
    return f'{{\n{out}}}'


def generate_diff(file1, file2):
    data_file1 = get_data(file1)
    data_file2 = get_data(file2)
    pars = parsing_files(data_file1, data_file2)
    out = format(pars)
    return out
# print(generate_diff('Test/file1.json', 'Test/file2.json'))
