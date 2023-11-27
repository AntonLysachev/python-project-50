from gendiff.cli import get_arguments
from gendiff.generate_diff import generate_diff


def main():
    file1_path, file2_path, style = get_arguments()
    print(generate_diff(file1_path, file2_path, style))


if __name__ == '__main__':
    main()
