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


def generate_diff(dict_1, dict_2):  # noqa: C901
    result = {}
    keys_1 = list(dict_1)
    keys_2 = list(dict_2)
    all_keys = list({x for x in keys_1 + keys_2})
    for key in sorted(all_keys):
        value_1 = dict_1.get(key)
        value_2 = dict_2.get(key)
        if value_1 == value_2:
            result[key] = {
                'status': 'unchanged',
                'value': value_1
            }
        elif (all([value_1, value_2])
              and isinstance(value_1, dict)
              and isinstance(value_2, dict)):
            result[key] = {
                'status': 'unchanged',
                'children1': value_1,
                'children2': value_2
            }
        elif (all([value_1, value_2])
              and value_1 != value_2
              and (not isinstance(value_1, dict)
                   or not isinstance(value_2, dict))):
            result[key] = {
                'status': 'changed',
                'value1': value_1,
                'value2': value_2
            }
        elif value_1 and not value_2:
            result[key] = {
                'status': 'deleted',
                'value': value_1
            }
        elif not value_1 and value_2:
            result[key] = {
                'status': 'added',
                'value': value_2
            }
    return result
