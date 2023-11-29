from gendiff.parsing import parsing
from gendiff.formatters.get_data import get_data
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
import json


def choice_format(format_name, parsing_file):
    match format_name:
        case 'plain':
            return '\n'.join(flatten(plain(parsing_file)))
        case 'stylish':
            return stylish(parsing_file)
        case 'json':
            return json.dumps(parsing_file, indent=2)


def flatten(tree):
    result = []

    def walk(subtree):
        for item in subtree:
            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)
    walk(tree)
    return result


def generate_diff(file1, file2, format_name='stylish'):
    data1 = get_data(file1)
    data2 = get_data(file2)
    match data2, data1:
        case None, _:
            return "Unknown format"
        case _, None:
            return "Unknown format"
        case _:
            parsing_file = parsing(data1, data2)
            return choice_format(format_name, parsing_file)
