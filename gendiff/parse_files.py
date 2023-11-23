import json
import yaml


def get_content(file):
    file_format = str(file).split('.')[-1]
    with open(file, 'r') as open_file:
        return parse(open_file.read(), file_format)


def parse(content, format):
    if format == 'json':
        return json.loads(content)
    elif format == 'yaml' or format == 'yml':
        return yaml.safe_load(content)
    else:
        raise ValueError(f'\'{format}\' format is not supported')
