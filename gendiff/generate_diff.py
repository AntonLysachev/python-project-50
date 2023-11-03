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


def styler(parsing_file):
    def style(parsing_file, space='', out=''):
        for key, value in parsing_file.items():
            if isinstance(value, dict):
                out = f'{out}    {space}{key}:'
                out = f'{out} {style(value, "    ")}\n'
            else:
                out = f'{out}  {space}{value}\n'
        return f'{{\n{out}{space}}}'
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
