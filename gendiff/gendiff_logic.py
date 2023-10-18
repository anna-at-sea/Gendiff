import json


def to_string(data):
    if isinstance(data, bool):
        return str(data).lower()
    return str(data)


def generate_diff(file_1, file_2):
    dict_1 = json.load(open(file_1))
    dict_2 = json.load(open(file_2))
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
