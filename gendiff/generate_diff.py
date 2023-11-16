from gendiff.parsing import parsing
from gendiff.get_date import get_date
from gendiff.stylish import stylish


def generate_diff(file1, file2):
    date1 = get_date(file1)
    date2 = get_date(file2)
    match date2, date1:
        case None, _:
            return "Unknown format"
        case _, None:
            return "Unknown format"
        case _:
            parsing_file = parsing(date1, date2)
            out = stylish(parsing_file)
            return out
