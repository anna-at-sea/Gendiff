import json
import yaml
import copy


def values_to_string(dict_tree):
    tree_copy = copy.deepcopy(dict_tree)

    def walk(node):
        for key, value in node.items():
            if isinstance(value, bool):
                node[key] = str(value).lower()
            elif value is None:
                node[key] = 'null'
            elif isinstance(value, dict):
                walk(value)
            else:
                node[key] = str(value)
        return node

    return walk(tree_copy)


def parse(file):
    if str(file).endswith('json'):
        return values_to_string(json.load(open(file)))
    elif str(file).endswith('yaml') or str(file).endswith('yml'):
        return values_to_string(yaml.safe_load(open(file)))
