from gendiff import generate_diff
import pytest
from os.path import join


FIXTURE_PATH = 'gendiff/tests/fixtures/'


def format_result(file_name):
    with open(
        join(FIXTURE_PATH, f'{file_name}.txt'), 'r'
    ) as open_path:
        return open_path.read()


@pytest.mark.parametrize(
    'input1, input2, format, expected',
    [
        ('file1.json', 'file2.json', 'stylish', 'diff_file1_file2'),
        ('file1.yaml', 'file2.yaml', 'stylish', 'diff_file1_file2'),
        ('file1.json', 'file1.json', 'stylish', 'diff_file1_file1'),
        ('file1.yaml', 'file1.yaml', 'stylish', 'diff_file1_file1'),
        ('empty.json', 'file1.json', 'stylish', 'diff_empty_file1'),
        ('empty.yaml', 'file1.yaml', 'stylish', 'diff_empty_file1'),
        ('file1.json', 'empty.json', 'stylish', 'diff_file1_empty'),
        ('file1.yaml', 'empty.yaml', 'stylish', 'diff_file1_empty'),
        ('empty.json', 'empty.json', 'stylish', 'diff_empty_stylish'),
        ('empty.yaml', 'empty.yaml', 'stylish', 'diff_empty_stylish'),
        ('nested1.json', 'nested2.json', 'stylish', 'diff_nested'),
        ('nested1.yaml', 'nested2.yaml', 'stylish', 'diff_nested'),
        ('file1.json', 'file2.json', 'plain', 'diff_plain_flat'),
        ('file1.yaml', 'file2.yaml', 'plain', 'diff_plain_flat'),
        ('empty.json', 'empty.json', 'plain', 'diff_empty_plain'),
        ('empty.yaml', 'empty.yaml', 'plain', 'diff_empty_plain'),
        ('nested1.json', 'nested2.json', 'plain', 'diff_plain_nested'),
        ('nested1.yaml', 'nested2.yaml', 'plain', 'diff_plain_nested')
    ]
)
def test_generate_diff(input1, input2, format, expected):
    assert generate_diff(
        join(FIXTURE_PATH, input1),
        join(FIXTURE_PATH, input2),
        format
    ) == format_result(expected)
