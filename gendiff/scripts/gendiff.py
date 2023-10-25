def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f FORMAT', '--format FORMAT', action='help', help='set format of output')
    args = parser.parse_args()
    print(args.indir)

if __name__ == '__main__':
    main()