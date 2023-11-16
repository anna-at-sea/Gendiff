#!/usr/bin/env python3


from gendiff import generate_diff
from gendiff.argparse import first_file, second_file, file_format


def main():
    print(generate_diff(first_file, second_file, file_format))


if __name__ == '__main__':
    main()
