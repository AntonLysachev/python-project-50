import argparse
from gendiff.generate_diff import generate_diff


def interface():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('filepath1', type=str)
    parser.add_argument('filepath2', type=str)
    parser.add_argument('-f', '--format',
                        dest='format',
                        action='store',
                        default='stylish',
                        type=str,
                        metavar='[type]',
                        help='output format (default: "stylish")')
    args = parser.parse_args()
    print(generate_diff(args.filepath1, args.filepath2, args.format))
