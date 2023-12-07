import json
import yaml
from os.path import splitext


def get_content(file):
    file_format = splitext(file)[-1]
    with open(file, 'r') as open_file:
        return parse(open_file.read(), file_format)


def parse(content, format):
    if format == '.json':
        return json.loads(content)
    elif format in ('.yaml', '.yml'):
        return yaml.safe_load(content)
    else:
        raise ValueError(f'\'{format}\' format is not supported')
