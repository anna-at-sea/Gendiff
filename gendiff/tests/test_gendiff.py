from gendiff import generate_diff, to_dict
import pytest


FILE1_JSON = to_dict('gendiff/tests/fixtures/json/file1.json')
FILE2_JSON = to_dict('gendiff/tests/fixtures/json/file2.json')
EMPTY_JSON = to_dict('gendiff/tests/fixtures/json/empty_file.json')
FILE1_YAML = to_dict('gendiff/tests/fixtures/yaml/file1.yaml')
FILE2_YAML = to_dict('gendiff/tests/fixtures/yaml/file2.yaml')
EMPTY_YAML = to_dict('gendiff/tests/fixtures/yaml/empty_file.yaml')
RESULT_FLAT = open('gendiff/tests/fixtures/txt/diff_file1_file2.txt', 'r')
RESULT_FLAT_SAME_FILE = open('gendiff/tests/fixtures/txt/diff_file1_file1.txt',
                             'r')
RESULT_EMPTY_FIRST = open('gendiff/tests/fixtures/txt/diff_empty_file1.txt',
                          'r')
RESULT_EMPTY_SECOND = open('gendiff/tests/fixtures/txt/diff_file1_empty.txt',
                           'r')
RESULT_BOTH_EMPTY = '{\n\n}'


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(FILE1_JSON, FILE2_JSON, RESULT_FLAT.read()),
     (FILE1_JSON, FILE1_JSON, RESULT_FLAT_SAME_FILE.read()),
     (EMPTY_JSON, FILE1_JSON, RESULT_EMPTY_FIRST.read()),
     (FILE1_JSON, EMPTY_JSON, RESULT_EMPTY_SECOND.read()),
     (EMPTY_JSON, EMPTY_JSON, RESULT_BOTH_EMPTY)
     ]
)
def test_gendiff_flat_json(input_1, input_2, expected):
    assert generate_diff(input_1, input_2) == expected


RESULT_FLAT.seek(0)
RESULT_FLAT_SAME_FILE.seek(0)
RESULT_EMPTY_FIRST.seek(0)
RESULT_EMPTY_SECOND.seek(0)


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(FILE1_YAML, FILE2_YAML, RESULT_FLAT.read()),
     (FILE1_YAML, FILE1_YAML, RESULT_FLAT_SAME_FILE.read()),
     (EMPTY_YAML, FILE1_YAML, RESULT_EMPTY_FIRST.read()),
     (FILE1_YAML, EMPTY_YAML, RESULT_EMPTY_SECOND.read()),
     (EMPTY_YAML, EMPTY_YAML, RESULT_BOTH_EMPTY)
     ]
)
def test_gendiff_flat_yaml(input_1, input_2, expected):
    assert generate_diff(input_1, input_2) == expected


RESULT_FLAT.close()
RESULT_FLAT_SAME_FILE.close()
RESULT_EMPTY_FIRST.close()
RESULT_EMPTY_SECOND.close()
