from gendiff.parse_files import parse
from gendiff.tests.fixtures.parse_results import (
    parse_result_flat, parse_result_nested
)
import pytest


json_path = 'gendiff/tests/fixtures/json/'
yaml_path = 'gendiff/tests/fixtures/yaml/'


@pytest.mark.parametrize(
    'input1, input2, expected',
    [(f'{json_path}file1.json', 'json', parse_result_flat),
     (f'{json_path}empty_file.json', 'json', {}),
     (f'{json_path}nested_file2.json', 'json', parse_result_nested)
     ]
)
def test_parse_json(input1, input2, expected):
    assert parse(input1, input2) == expected


@pytest.mark.parametrize(
    'input1, input2, expected',
    [(f'{yaml_path}file1.yaml', 'yaml', parse_result_flat),
     (f'{yaml_path}empty_file.yaml', 'yaml', {}),
     (f'{yaml_path}nested_file2.yaml', 'yaml', parse_result_nested)
     ]
)
def test_parse_yaml(input1, input2, expected):
    assert parse(input1, input2) == expected
