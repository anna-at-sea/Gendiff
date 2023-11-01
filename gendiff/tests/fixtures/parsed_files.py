from gendiff.parse_files import parse


FILE1_JSON = parse('gendiff/tests/fixtures/json/file1.json')
FILE2_JSON = parse('gendiff/tests/fixtures/json/file2.json')
EMPTY_JSON = parse('gendiff/tests/fixtures/json/empty_file.json')
FILE1_YAML = parse('gendiff/tests/fixtures/yaml/file1.yaml')
FILE2_YAML = parse('gendiff/tests/fixtures/yaml/file2.yaml')
EMPTY_YAML = parse('gendiff/tests/fixtures/yaml/empty_file.yaml')
NESTED_FILE1_JSON = parse('gendiff/tests/fixtures/json/nested_file1.json')
NESTED_FILE2_JSON = parse('gendiff/tests/fixtures/json/nested_file2.json')
NESTED_FILE1_YAML = parse('gendiff/tests/fixtures/yaml/nested_file1.yaml')
NESTED_FILE2_YAML = parse('gendiff/tests/fixtures/yaml/nested_file2.yaml')
