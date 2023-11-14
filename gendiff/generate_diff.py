import json
import yaml
from gendiff.parsing import parsing
from gendiff.define_format import define


def get_data(file):
    format = define(file)
    if format == 'json':
        with open(file, "r") as f:
            return json.load(f)
    if format == 'yml':
        with open(file, "r") as f:
            return yaml.full_load(f)


def print_dict(node, space, deep, out=''):
    space = '  ' * deep
    down_space = '  ' * (deep - 2)
    for key, value in node.items():
        if isinstance(value, dict):
            out = f'{out}{space}{key}: '
            out = f'{out}{print_dict(value, space, deep + 2)}\n'
        else:
            out = f'{out}{space}{key}: {value}\n'
    return f'{{\n{out}{down_space}}}'


def styler(parsing_file):
    def style(parsing_file, deep=1, out=''):
        space = '  ' * deep
        down_space = '  ' * (deep - 1)
        for key, value in parsing_file.items():
            if value.get('children'):
                out = f'{out}{space}{key}:'
                out = f'{out} {style(value["children"], deep + 1)}\n'
                continue
            if value['value1'] == value['value2']:
                out = f'{out}{space}  {key}: {value["value1"]}\n'
            elif value['value2'] == None:
                if isinstance(value['value1'], dict):
                    out = f'{out}{space}- {key}: '
                    out = f'{out}{print_dict(value["value1"], space, deep + 3)}\n'
                else:
                    out = f'{out}{space}- {key}: {value["value1"]}\n'
            elif value['value1'] == None:
                if isinstance(value['value2'], dict):
                    out = f'{out}{space}+ {key}: '
                    out = f'{out}{print_dict(value["value2"], space, deep + 3)}\n'
                else:    
                    out = f'{out}{space}+ {key}: {value["value2"]}\n'
            else:
                if isinstance(value['value1'], dict):
                    out = f'{out}{space}- {key}: '
                    out = f'{out}{print_dict(value["value1"], space, deep + 3)}\n'
                    out = f'{out}{space}+ {key}: {value["value2"]}\n'
                    continue
                if isinstance(value['value2'], dict):
                    out = f'{out}{space}+ {key}: '
                    out = f'{out}{print_dict(value["value2"], space, deep + 3)}\n'
                    out = f'{out}{space}- {key}: {value["value1"]}\n'
                    continue
                out = f'{out}{space}- {key}: {value["value1"]}\n'
                out = f'{out}{space}+ {key}: {value["value2"]}\n'
        return f'{{\n{out}{down_space}}}'
    out = style(parsing_file)
    return out


def generate_diff(file1, file2):
    date1 = get_data(file1)
    date2 = get_data(file2)
    match date2, date1:
        case None, _:
            return "Unknown format"
        case _, None:
            return "Unknown format"
        case _:
            parsing_file = parsing(date1, date2)
            out = styler(parsing_file)
            return out
