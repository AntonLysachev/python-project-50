from gendiff.parsing import parsing


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
    parsing_file = parsing(file1, file2)
    print = styler(parsing_file)
    return print
