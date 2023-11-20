from gendiff.parse_files import parse, get_content
from gendiff.tests.fixtures.parse_results import (
    parse_result_flat, parse_result_nested
)
import pytest


json_path = 'gendiff/tests/fixtures/json/'
yaml_path = 'gendiff/tests/fixtures/yaml/'


@pytest.mark.parametrize(
    'input1, input2, expected',
    [(get_content(f'{json_path}file1.json'), 'json', parse_result_flat),
     (get_content(f'{json_path}empty.json'), 'json', {}),
     (get_content(f'{json_path}nested2.json'), 'json', parse_result_nested)
     ]
)
def test_parse_json(input1, input2, expected):
    assert parse(input1, input2) == expected


@pytest.mark.parametrize(
    'input1, input2, expected',
    [(get_content(f'{yaml_path}file1.yaml'), 'yaml', parse_result_flat),
     (get_content(f'{yaml_path}empty.yaml'), 'yaml', {}),
     (get_content(f'{yaml_path}nested2.yaml'), 'yaml', parse_result_nested)
     ]
)
def test_parse_yaml(input1, input2, expected):
    assert parse(input1, input2) == expected
