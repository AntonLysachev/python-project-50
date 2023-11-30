from gendiff.parsing import analyze
from gendiff.file_reader import get_data
from gendiff.formatters.switch import select_format


def generate_diff(file1, file2, format_name='stylish'):
    data1 = get_data(file1)
    data2 = get_data(file2)
    match data2, data1:
        case None, _:
            return "Unknown format"
        case _, None:
            return "Unknown format"
        case _:
            parsing_file = analyze(data1, data2)
            return select_format(format_name, parsing_file)
