from gendiff.parse_files import parse


FILE1_JSON = parse('gendiff/tests/fixtures/json/file1.json')
FILE2_JSON = parse('gendiff/tests/fixtures/json/file2.json')
EMPTY_JSON = parse('gendiff/tests/fixtures/json/empty_file.json')
FILE1_YAML = parse('gendiff/tests/fixtures/yaml/file1.yaml')
FILE2_YAML = parse('gendiff/tests/fixtures/yaml/file2.yaml')
EMPTY_YAML = parse('gendiff/tests/fixtures/yaml/empty_file.yaml')
