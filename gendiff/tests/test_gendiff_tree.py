from gendiff import generate_diff_tree
from gendiff.parse_files import get_content
from gendiff.tests.fixtures.diff_results import (
    diff_flat, diff_both_empty, diff_nested
)
import pytest


def get_input(file_name):
    if file_name.endswith('json'):
        return get_content(f'gendiff/tests/fixtures/json/{file_name}')
    elif file_name.endswith('yaml') or file_name.endswith('yml'):
        return get_content(f'gendiff/tests/fixtures/yaml/{file_name}')


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [('file1.json', 'file2.json', diff_flat),
     ('empty.json', 'empty.json', diff_both_empty),
     ('file1.yaml', 'file2.yaml', diff_flat),
     ('empty.yaml', 'empty.yaml', diff_both_empty),
     ('nested1.json', 'nested2.json', diff_nested),
     ('nested1.yaml', 'nested2.yaml', diff_nested)
     ]
)
def test_generate_diff_tree(input_1, input_2, expected):
    assert (generate_diff_tree(get_input(input_1), get_input(input_2))
            == expected)
