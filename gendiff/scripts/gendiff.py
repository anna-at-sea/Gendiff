#!/usr/bin/env python3


from gendiff import generate_diff
from gendiff.parse_args import get_args


def main():
    print(generate_diff(*get_args()))


if __name__ == '__main__':
    main()
