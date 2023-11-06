#!/usr/bin/env python3


from gendiff import generate_diff
from gendiff.stylish import stylish
from gendiff.parse_files import parse
import argparse


parser = argparse.ArgumentParser(description='Compares \
two configuration files and shows a difference.')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def main():
    print(
        stylish(generate_diff(parse(args.first_file), parse(args.second_file)))
    )


if __name__ == '__main__':
    main()
