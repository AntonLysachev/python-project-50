import json
import copy


def get_data(file):
    with open(file, "r") as f:
        date = json.load(f)
    return date


def parsing(file1, file2):
    date_file1 = get_data(file1)
    date_file2 = get_data(file2)
    merg = copy.deepcopy(date_file1)
    merg.update(date_file2)

    def pars(merg_date, date1, date2):
        parsing = {}
        for key, value in merg_date.items():
            if key in date1 and key in date2:
                if isinstance(value, dict):
                    parsing.update({key: pars(value, date1[key], date2[key])})
                    continue
                if date1[key] == date2[key]:
                    parsing.update({key: f'  {key}: {date1[key]}'})
                    continue
                parsing.update({f'{key}1': f'- {key}: {date1[key]}',
                                f'{key}2': f'+ {key}: {date2[key]}'})
                continue
            else:
                if key in date1:
                    parsing.update({key: f'- {key}: {date1[key]}'})
                    continue
                parsing.update({key: f'+ {key}: {date2[key]}'})
        return parsing
    out = pars(merg, date_file1, date_file2)
    return dict(sorted(out.items()))
