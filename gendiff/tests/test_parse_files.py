from gendiff.parse_files import get_content
from gendiff.tests.fixtures.parse_results import (
    parse_result_flat, parse_result_nested
)
import pytest


json_path = 'gendiff/tests/fixtures/json/'
yaml_path = 'gendiff/tests/fixtures/yaml/'


@pytest.mark.parametrize(
    'input, expected',
    [(f'{json_path}file1.json', parse_result_flat),
     (f'{json_path}empty.json', {}),
     (f'{json_path}nested2.json', parse_result_nested)
     ]
)
def test_parse_json(input, expected):
    assert get_content(input) == expected


@pytest.mark.parametrize(
    'input, expected',
    [(f'{yaml_path}file1.yaml', parse_result_flat),
     (f'{yaml_path}empty.yaml', {}),
     (f'{yaml_path}nested2.yaml', parse_result_nested)
     ]
)
def test_parse_yaml(input, expected):
    assert get_content(input) == expected


def test_parse_wrong_format():
    with pytest.raises(ValueError):
        get_content('gendiff/tests/fixtures/txt/diff_nested.txt')
