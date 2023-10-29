from gendiff.parse_files import parse
import pytest


RESULT = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False
}


@pytest.mark.parametrize(
    'input, expected',
    [('gendiff/tests/fixtures/json/file1.json', RESULT),
     ('gendiff/tests/fixtures/json/empty_file.json', {})
     ]
)
def test_parse_json(input, expected):
    assert parse(input) == expected


@pytest.mark.parametrize(
    'input, expected',
    [('gendiff/tests/fixtures/yaml/file1.yaml', RESULT),
     ('gendiff/tests/fixtures/yaml/empty_file.yaml', {})
     ]
)
def test_parse_yaml(input, expected):
    assert parse(input) == expected
