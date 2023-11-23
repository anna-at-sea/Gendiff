#!/usr/bin/env python3


from gendiff import generate_diff
from gendiff.cli import get_args


def main():
    print(generate_diff(
        get_args().first_file,
        get_args().second_file,
        get_args().format
    ))


if __name__ == '__main__':
    main()
