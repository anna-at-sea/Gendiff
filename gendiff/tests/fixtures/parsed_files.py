from gendiff.parse_files import parse


json_path = 'gendiff/tests/fixtures/json/'
yaml_path = 'gendiff/tests/fixtures/yaml/'


FILE1_JSON = parse(f'{json_path}file1.json', 'json')
FILE2_JSON = parse(f'{json_path}file2.json', 'json')
EMPTY_JSON = parse(f'{json_path}empty_file.json', 'json')
FILE1_YAML = parse(f'{yaml_path}file1.yaml', 'yaml')
FILE2_YAML = parse(f'{yaml_path}file2.yaml', 'yaml')
EMPTY_YAML = parse(f'{yaml_path}empty_file.yaml', 'yaml')
NESTED_FILE1_JSON = parse(f'{json_path}nested_file1.json', 'yaml')
NESTED_FILE2_JSON = parse(f'{json_path}nested_file2.json', 'yaml')
NESTED_FILE1_YAML = parse(f'{yaml_path}nested_file1.yaml', 'yaml')
NESTED_FILE2_YAML = parse(f'{yaml_path}nested_file2.yaml', 'yaml')
