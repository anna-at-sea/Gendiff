from gendiff.gendiff_logic import generate_diff_tree
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_formatter import json_formatter
from gendiff.load_data import get_content

__all__ = ('generate_diff', 'generate_diff_tree', 'stylish',
           'get_content', 'plain', 'json_formatter')


formatters = {'stylish': stylish, 'plain': plain, 'json': json_formatter}


def generate_diff(first_file, second_file, formatter='stylish'):
    return formatters[formatter](
        generate_diff_tree(
            get_content(first_file),
            get_content(second_file)
        )
    )
