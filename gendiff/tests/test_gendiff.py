from gendiff import generate_diff
import pytest


FILE1_JSON = 'gendiff/tests/fixtures/file1.json'
FILE2_JSON = 'gendiff/tests/fixtures/file2.json'
EMPTY_JSON = 'gendiff/tests/fixtures/empty_file.json'
RESULT_FLAT = open('gendiff/tests/fixtures/file1_file2_diff.txt', 'r')
RESULT_FLAT_SAME_FILE = open('gendiff/tests/fixtures/file1_file1_diff.txt', 'r')
EMPTY_FIRST_RESULT = open('gendiff/tests/fixtures/empty_file1_diff.txt', 'r')
EMPTY_SECOND_RESULT = open('gendiff/tests/fixtures/file1_empty_diff.txt', 'r')
BOTH_EMPTY_RESULT = '{\n\n}'


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(FILE1_JSON, FILE2_JSON, RESULT_FLAT.read()),
     (FILE1_JSON, FILE1_JSON, RESULT_FLAT_SAME_FILE.read()),
     (EMPTY_JSON, FILE1_JSON, EMPTY_FIRST_RESULT.read()),
     (FILE1_JSON, EMPTY_JSON, EMPTY_SECOND_RESULT.read()),
     (EMPTY_JSON, EMPTY_JSON, BOTH_EMPTY_RESULT)
     ]
)
def test_gendiff_flat_json(input_1, input_2, expected):
    assert generate_diff(input_1, input_2) == expected


RESULT_FLAT.close()
RESULT_FLAT_SAME_FILE.close()
EMPTY_FIRST_RESULT.close()
EMPTY_SECOND_RESULT.close()
