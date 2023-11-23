from gendiff import generate_diff
import pytest


def format_result(file_name):
    if file_name == '{\n\n}':
        return '{\n\n}'
    elif file_name == '':
        return ''
    with open(f'gendiff/tests/fixtures/txt/{file_name}.txt', 'r') as open_path:
        return open_path.read()


json_path = 'gendiff/tests/fixtures/json/'
yaml_path = 'gendiff/tests/fixtures/yaml/'


@pytest.mark.parametrize(
    'input1, input2, format, expected',
    [('file1.json', 'file2.json', 'stylish', 'diff_file1_file2'),
     ('file1.json', 'file1.json', 'stylish', 'diff_file1_file1'),
     ('empty.json', 'file1.json', 'stylish', 'diff_empty_file1'),
     ('file1.json', 'empty.json', 'stylish', 'diff_file1_empty'),
     ('empty.json', 'empty.json', 'stylish', '{\n\n}'),
     ('nested1.json', 'nested2.json', 'stylish', 'diff_nested'),
     ('file1.json', 'file2.json', 'plain', 'diff_plain_flat'),
     ('empty.json', 'empty.json', 'plain', ''),
     ('nested1.json', 'nested2.json', 'plain', 'diff_plain_nested')
     ]
)
def test_generate_diff_json(input1, input2, format, expected):
    assert (generate_diff(json_path + input1, json_path + input2, format)
            == format_result(expected))


@pytest.mark.parametrize(
    'input1, input2, format, expected',
    [('file1.yaml', 'file2.yaml', 'stylish', 'diff_file1_file2'),
     ('file1.yaml', 'file1.yaml', 'stylish', 'diff_file1_file1'),
     ('empty.yaml', 'file1.yaml', 'stylish', 'diff_empty_file1'),
     ('file1.yaml', 'empty.yaml', 'stylish', 'diff_file1_empty'),
     ('empty.yaml', 'empty.yaml', 'stylish', '{\n\n}'),
     ('nested1.yaml', 'nested2.yaml', 'stylish', 'diff_nested'),
     ('file1.yaml', 'file2.yaml', 'plain', 'diff_plain_flat'),
     ('empty.yaml', 'empty.yaml', 'plain', ''),
     ('nested1.yaml', 'nested2.yaml', 'plain', 'diff_plain_nested')
     ]
)
def test_generate_diff_yaml(input1, input2, format, expected):
    assert (generate_diff(yaml_path + input1, yaml_path + input2, format)
            == format_result(expected))
