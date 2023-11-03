# def generate_diff(dict_1, dict_2):
#     result = []
#     all_keys = list(set(list(dict_1) + list(dict_2)))
#     for key in sorted(all_keys):
#         value_1 = to_string(dict_1.get(key))
#         value_2 = to_string(dict_2.get(key))
#         if key in dict_1.keys() and key in dict_2.keys():
#             if dict_1[key] == dict_2[key]:
#                 result.append(f'    {key}: {value_1}')
#             else:
#                 result.append(f'  - {key}: {value_1}')
#                 result.append(f'  + {key}: {value_2}')
#         elif key in dict_1.keys():
#             result.append(f'  - {key}: {value_1}')
#         elif key in dict_2.keys():
#             result.append(f'  + {key}: {value_2}')
#     return '{\n' + '\n'.join(result) + '\n}'
def get_all_keys(*dicts):
    return sorted(list({y for x in dicts for y in list(x)}))


def _values_are_dicts(value_1, value_2):
    return (value_1 is not None
            and value_2 is not None
            and isinstance(value_1, dict)
            and isinstance(value_2, dict))


def _value_changed(value_1, value_2):
    return (value_1 is not None
            and value_2 is not None
            and value_1 != value_2
            and (not isinstance(value_1, dict)
                 or not isinstance(value_2, dict)))


def _value_deleted(value_1, value_2):
    return value_1 and value_2 is None


def _value_added(value_1, value_2):
    return value_1 is None and value_2


def generate_description(value_1, value_2):
    if value_1 == value_2:
        return {
            'status': 'unchanged',
            'value': value_1
        }
    elif _values_are_dicts(value_1, value_2):
        return {
            'status': 'unchanged',
            'children': generate_diff(value_1, value_2)
        }
    elif _value_changed(value_1, value_2):
        return {
            'status': 'changed',
            'value1': value_1,
            'value2': value_2
        }
    elif _value_deleted(value_1, value_2):
        return {
            'status': 'deleted',
            'value': value_1
        }
    elif _value_added(value_1, value_2):
        return {
            'status': 'added',
            'value': value_2
        }


def generate_diff(dict_1, dict_2):
    result = {}
    all_keys = get_all_keys(dict_1, dict_2)
    for key in all_keys:
        value_1 = dict_1.get(key)
        value_2 = dict_2.get(key)
        result[key] = generate_description(value_1, value_2)
    return result
