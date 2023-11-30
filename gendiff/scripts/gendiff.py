from gendiff.cli import get_arguments
from gendiff.generator import generate_diff


def main():
    args = get_arguments()
    print(generate_diff(args.filepath1, args.filepath2, args.format))


if __name__ == '__main__':
    main()
