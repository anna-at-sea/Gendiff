from gendiff import generate_diff


FILE1_JSON = 'gendiff/tests/fixtures/file1.json'
FILE2_JSON = 'gendiff/tests/fixtures/file2.json'
EMPTY_JSON = 'gendiff/tests/fixtures/empty_file.json'


def test_gendiff_flat_json():
    result = open('gendiff/tests/fixtures/file1_file2_diff.txt', 'r')
    assert generate_diff(FILE1_JSON, FILE2_JSON) == result.read()
    result.close()


def test_gendiff_flat_json_same_file():
    result = open('gendiff/tests/fixtures/file1_file1_diff.txt', 'r')
    assert generate_diff(FILE1_JSON, FILE1_JSON) == result.read()
    result.close()


def test_gendiff_flat_json_empty():
    empty_first_result = open('gendiff/tests/fixtures/empty_file1_diff.txt',
                              'r')
    empty_second_result = open('gendiff/tests/fixtures/file1_empty_diff.txt',
                               'r')
    both_empty_result = '{\n\n}'
    assert generate_diff(EMPTY_JSON, FILE1_JSON) == empty_first_result.read()
    assert generate_diff(FILE1_JSON, EMPTY_JSON) == empty_second_result.read()
    assert generate_diff(EMPTY_JSON, EMPTY_JSON) == both_empty_result
    empty_first_result.close()
    empty_second_result.close()
