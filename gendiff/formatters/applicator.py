from gendiff.formatters.plain_format import form_plain
from gendiff.formatters.stylish import form_tree
from gendiff.formatters.json_format import form_json


def apply_format(format_name, dict_diff):
    match format_name:
        case 'plain':
            return form_plain(dict_diff)
        case 'stylish':
            return form_tree(dict_diff)
        case 'json':
            return form_json(dict_diff)
        case _:
            raise ValueError('Invalid format entered')
