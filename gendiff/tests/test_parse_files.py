from gendiff.parse_files import parse
import pytest


RESULT_FLAT = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False
}


RESULT_NESTED = {
    'common': {
        'follow': False,
        'setting1': 'Value 1',
        'setting3': None,
        'setting4': 'blah blah',
        'setting5': {
            'key5': 'value5'
        },
        'setting6': {
            'key': 'value',
            'ops': 'vops',
            'doge': {
                'wow': 'so much'
            }
        }
    },
    'group1': {
        'foo': 'bar',
        'baz': 'bars',
        'nest': 'str'
    },
    'group3': {
        'deep': {
            'id': {
                'number': 45
            }
        },
        'fee': 100500
    }
}


@pytest.mark.parametrize(
    'input, expected',
    [('gendiff/tests/fixtures/json/file1.json', RESULT_FLAT),
     ('gendiff/tests/fixtures/json/empty_file.json', {}),
     ('gendiff/tests/fixtures/json/nested_file2.json', RESULT_NESTED)
     ]
)
def test_parse_json(input, expected):
    assert parse(input) == expected


@pytest.mark.parametrize(
    'input, expected',
    [('gendiff/tests/fixtures/yaml/file1.yaml', RESULT_FLAT),
     ('gendiff/tests/fixtures/yaml/empty_file.yaml', {}),
     ('gendiff/tests/fixtures/yaml/nested_file2.yaml', RESULT_NESTED)
     ]
)
def test_parse_yaml(input, expected):
    assert parse(input) == expected
