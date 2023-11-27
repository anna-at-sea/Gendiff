from gendiff import generate_diff
import pytest
from os.path import join


TXT_PATH = 'gendiff/tests/fixtures/txt/'
JSON_PATH = 'gendiff/tests/fixtures/json/'
YAML_PATH = 'gendiff/tests/fixtures/yaml/'


def format_result(file_name):
    if file_name == '{\n\n}':
        return '{\n\n}'
    elif file_name == '':
        return ''
    with open(
        join(TXT_PATH, f'{file_name}.txt'), 'r'
    ) as open_path:
        return open_path.read()


tested_cases = [
    ('file1', 'file2', 'stylish', 'diff_file1_file2'),
    ('file1', 'file1', 'stylish', 'diff_file1_file1'),
    ('empty', 'file1', 'stylish', 'diff_empty_file1'),
    ('file1', 'empty', 'stylish', 'diff_file1_empty'),
    ('empty', 'empty', 'stylish', '{\n\n}'),
    ('nested1', 'nested2', 'stylish', 'diff_nested'),
    ('file1', 'file2', 'plain', 'diff_plain_flat'),
    ('empty', 'empty', 'plain', ''),
    ('nested1', 'nested2', 'plain', 'diff_plain_nested')
]


@pytest.mark.parametrize(
    'input1, input2, format, expected',
    tested_cases
)
def test_generate_diff_json(input1, input2, format, expected):
    assert generate_diff(
        join(JSON_PATH, input1 + '.json'),
        join(JSON_PATH, input2 + '.json'),
        format
    ) == format_result(expected)


@pytest.mark.parametrize(
    'input1, input2, format, expected',
    tested_cases
)
def test_generate_diff_yaml(input1, input2, format, expected):
    assert generate_diff(
        join(YAML_PATH, input1 + '.yaml'),
        join(YAML_PATH, input2 + '.yaml'),
        format
    ) == format_result(expected)
