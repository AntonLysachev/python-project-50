from gendiff.comparison import get_diff
from gendiff.file_reader import get_data
from gendiff.formatters.switch import apply_format


def generate_diff(file1, file2, format_name='stylish'):
    data1 = get_data(file1)
    data2 = get_data(file2)
    parsing_file = get_diff(data1, data2)
    return apply_format(format_name, parsing_file)
