import argparse


def get_arguments():
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
    return parser.parse_args()
