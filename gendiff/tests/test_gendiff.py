from gendiff import generate_diff_tree
from gendiff.parse_files import parse, get_content, get_format
from gendiff.tests.fixtures.diff_results import (
    diff_flat, diff_flat_same_file, diff_empty_first,
    diff_empty_second, diff_both_empty, diff_nested
)
import pytest


def get_input(file_name):
    file_format = get_format(file_name)
    if file_format == 'json':
        return parse(
            get_content(f'gendiff/tests/fixtures/json/{file_name}'), 'json'
        )
    elif file_format in ('yaml', 'yml'):
        return parse(
            get_content(f'gendiff/tests/fixtures/yaml/{file_name}'), 'yaml'
        )


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(get_input('file1.json'), get_input('file2.json'), diff_flat),
     (get_input('file1.json'), get_input('file1.json'), diff_flat_same_file),
     (get_input('empty.json'), get_input('file1.json'), diff_empty_first),
     (get_input('file1.json'), get_input('empty.json'), diff_empty_second),
     (get_input('empty.json'), get_input('empty.json'), diff_both_empty)
     ]
)
def test_gendiff_flat_json(input_1, input_2, expected):
    assert generate_diff_tree(input_1, input_2) == expected


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(get_input('file1.yaml'), get_input('file2.yaml'), diff_flat),
     (get_input('file1.yaml'), get_input('file1.yaml'), diff_flat_same_file),
     (get_input('empty.yaml'), get_input('file1.yaml'), diff_empty_first),
     (get_input('file1.yaml'), get_input('empty.yaml'), diff_empty_second),
     (get_input('empty.yaml'), get_input('empty.yaml'), diff_both_empty)
     ]
)
def test_gendiff_flat_yaml(input_1, input_2, expected):
    assert generate_diff_tree(input_1, input_2) == expected


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(get_input('nested1.json'), get_input('nested2.json'), diff_nested),
     (get_input('nested1.yaml'), get_input('nested2.yaml'), diff_nested)
     ]
)
def test_gendiff_nested(input_1, input_2, expected):
    assert generate_diff_tree(input_1, input_2) == expected
