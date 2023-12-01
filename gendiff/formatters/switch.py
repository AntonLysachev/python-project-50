from gendiff.formatters.plain_format import form_plain
from gendiff.formatters.stylish import form_tree
from gendiff.formatters.json_format import form_json


def apply_format(format_name, parsing_file):
    match format_name:
        case 'plain':
            return form_plain(parsing_file)
        case 'stylish':
            return form_tree(parsing_file)
        case 'json':
            return form_json(parsing_file)
        case _:
            return 'Invalid format entered'
