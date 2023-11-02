import json


def get_data(file):
    with open(file, "r") as f:
        date = json.load(f)
    return date


def parsing(file1, file2):
    date1 = get_data(file1)
    date2 = get_data(file2)
    parsing = {}
    for key in date1.keys():
        if date1[key] == date2.get(key):
            parsing.update({key: f'  {key}: {date1[key]}'})
        else:
            parsing.update({key: f'- {key}: {date1[key]}'})
    for key in date2.keys():
        if date2[key] != date1.get(key):
            parsing.update({f'{key}2': f'+ {key}: {date2[key]}'})
    return dict(sorted(parsing.items()))
