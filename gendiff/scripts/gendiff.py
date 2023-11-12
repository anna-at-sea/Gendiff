#!/usr/bin/env python3


from gendiff import generate_diff, stylish, plain
import argparse


parser = argparse.ArgumentParser(description='Compares \
two configuration files and shows a difference.')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output',
                    default='stylish')
args = parser.parse_args()


formats = {'stylish': stylish, 'plain': plain}


def main():
    print(
        generate_diff(
            args.first_file, args.second_file, formats[args.format]
        )
    )


if __name__ == '__main__':
    main()
