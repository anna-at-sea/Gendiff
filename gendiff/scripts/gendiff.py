#!/usr/bin/env python3


from gendiff import generate_diff
import argparse


parser = argparse.ArgumentParser(description='Compares \
two configuration files and shows a difference.')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def main():
    print(generate_diff(args.first_file, args.second_file))
    # gendiff/json_files/file1.json gendiff/json_files/file2.json


if __name__ == '__main__':
    main()
