import json
import yaml


def get_content_json(file):
    with open(file) as open_file:
        result = json.load(open_file)
    return result


def get_content_yaml(file):
    with open(file) as open_file:
        result = yaml.safe_load(open_file)
    return result


def parse(content, format):
    if format == 'json':
        return get_content_json(content)
    elif format == 'yaml' or format == 'yml':
        return get_content_yaml(content)
