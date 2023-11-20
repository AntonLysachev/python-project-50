from gendiff.parsing import parsing
from gendiff.get_data import get_data
from gendiff.stylish import stylish
from gendiff.plain import plain


def generate_diff(file1, file2, format_name=''):
    data1 = get_data(file1)
    data2 = get_data(file2)
    match data2, data1:
        case None, _:
            return "Unknown format"
        case _, None:
            return "Unknown format"
        case _:
            parsing_file = parsing(data1, data2)
            match format_name:
                case 'plain':
                    out = plain(parsing_file)
                case _:
                    out = stylish(parsing_file)
            return out
