from gendiff import generate_diff_tree
from gendiff.parse_files import parse
from gendiff.tests.fixtures.diff_results import (
    diff_flat, diff_flat_same_file, diff_empty_first,
    diff_empty_second, diff_both_empty, diff_nested
)
import pytest


json_path = 'gendiff/tests/fixtures/json/'
yaml_path = 'gendiff/tests/fixtures/yaml/'


file1_json = parse(f'{json_path}file1.json', 'json')
file2_json = parse(f'{json_path}file2.json', 'json')
empty_json = parse(f'{json_path}empty_file.json', 'json')
file1_yaml = parse(f'{yaml_path}file1.yaml', 'yaml')
file2_yaml = parse(f'{yaml_path}file2.yaml', 'yaml')
empty_yaml = parse(f'{yaml_path}empty_file.yaml', 'yaml')
nested_file1_json = parse(f'{json_path}nested_file1.json', 'yaml')
nested_file2_json = parse(f'{json_path}nested_file2.json', 'yaml')
nested_file1_yaml = parse(f'{yaml_path}nested_file1.yaml', 'yaml')
nested_file2_yaml = parse(f'{yaml_path}nested_file2.yaml', 'yaml')


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(file1_json, file2_json, diff_flat),
     (file1_json, file1_json, diff_flat_same_file),
     (empty_json, file1_json, diff_empty_first),
     (file1_json, empty_json, diff_empty_second),
     (empty_json, empty_json, diff_both_empty)
     ]
)
def test_gendiff_flat_json(input_1, input_2, expected):
    assert generate_diff_tree(input_1, input_2) == expected


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(file1_yaml, file2_yaml, diff_flat),
     (file1_yaml, file1_yaml, diff_flat_same_file),
     (empty_yaml, file1_yaml, diff_empty_first),
     (file1_yaml, empty_yaml, diff_empty_second),
     (empty_yaml, empty_yaml, diff_both_empty)
     ]
)
def test_gendiff_flat_yaml(input_1, input_2, expected):
    assert generate_diff_tree(input_1, input_2) == expected


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(nested_file1_json, nested_file2_json, diff_nested),
     (nested_file1_yaml, nested_file2_yaml, diff_nested)
     ]
)
def test_gendiff_nested(input_1, input_2, expected):
    assert generate_diff_tree(input_1, input_2) == expected
