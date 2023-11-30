from gendiff.formatters.plain_format import print_plain
from gendiff.formatters.tree_format import print_tree
from gendiff.formatters.json_format import print_json


def select_format(format_name, parsing_file):
    match format_name:
        case 'plain':
            return print_plain(parsing_file)
        case 'stylish':
            return print_tree(parsing_file)
        case 'json':
            return print_json(parsing_file)
