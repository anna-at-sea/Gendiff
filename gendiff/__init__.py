from gendiff.gendiff_logic import generate_diff
from gendiff.stylish import stylish
from gendiff.parse_files import parse

__all__ = ('gendiff', 'generate_diff', 'stylish', 'parse')


def gendiff(first_file, second_file, format=stylish):
    return format(generate_diff(parse(first_file), parse(second_file)))
