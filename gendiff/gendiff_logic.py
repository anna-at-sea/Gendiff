import json
import yaml


def to_string(data):
    if isinstance(data, bool):
        return str(data).lower()
    return str(data)


def to_dict(file):
    if str(file).endswith('json'):
        return json.load(open(file))
    elif str(file).endswith('yaml') or str(file).endswith('yml'):
        return yaml.safe_load(open(file))


def generate_diff(dict_1, dict_2):
    result = []
    all_keys = list(set(list(dict_1) + list(dict_2)))
    for key in sorted(all_keys):
        value_1 = to_string(dict_1.get(key))
        value_2 = to_string(dict_2.get(key))
        if key in dict_1.keys() and key in dict_2.keys():
            if dict_1[key] == dict_2[key]:
                result.append(f'    {key}: {value_1}')
            else:
                result.append(f'  - {key}: {value_1}')
                result.append(f'  + {key}: {value_2}')
        elif key in dict_1.keys():
            result.append(f'  - {key}: {value_1}')
        elif key in dict_2.keys():
            result.append(f'  + {key}: {value_2}')
    return '{\n' + '\n'.join(result) + '\n}'
