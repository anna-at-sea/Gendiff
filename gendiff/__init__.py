from gendiff.gendiff_logic import generate_diff_tree
from gendiff.formats.stylish import stylish
from gendiff.formats.plain import plain
from gendiff.formats.json import json_format
from gendiff.parse_files import parse

__all__ = ('generate_diff', 'generate_diff_tree', 'stylish',
           'parse', 'plain', 'json_format')


formats = {'stylish': stylish, 'plain': plain, 'json': json_format}


def generate_diff(first_file, second_file, format_name='stylish'):
    return formats[format_name](
        generate_diff_tree(
            parse(first_file), parse(second_file)
        )
    )
