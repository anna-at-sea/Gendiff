import json
import yaml


def get_content(file):
    with open(file, 'r') as open_file:
        return open_file.read()


def get_format(file):
    return str(file).split('.')[-1]


def parse(content, format):
    if format == 'json':
        return json.loads(content)
    elif format == 'yaml' or format == 'yml':
        return yaml.safe_load(content)
