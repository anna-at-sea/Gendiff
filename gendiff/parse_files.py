import json
import yaml


def parse(file):
    if str(file).endswith('json'):
        return json.load(open(file))
    elif str(file).endswith('yaml') or str(file).endswith('yml'):
        return yaml.safe_load(open(file))
