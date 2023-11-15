def _values_are_dicts(value_1, value_2):
    return (isinstance(value_1, dict)
            and isinstance(value_2, dict))


def _value_changed(value_1, value_2):
    return (value_1 != 'value not found'
            and value_2 != 'value not found'
            and value_1 != value_2
            and (not isinstance(value_1, dict)
                 or not isinstance(value_2, dict)))


def generate_description(key, value_1, value_2):
    if value_1 == value_2:
        return {
            'name': key,
            'status': 'unchanged',
            'value': value_1
        }
    elif _values_are_dicts(value_1, value_2):
        return {
            'name': key,
            'status': 'unchanged',
            'children': generate_children(value_1, value_2)
        }
    elif _value_changed(value_1, value_2):
        return {
            'name': key,
            'status': 'changed',
            'value': value_1,
            'value2': value_2
        }
    elif value_2 == 'value not found':
        return {
            'name': key,
            'status': 'deleted',
            'value': value_1
        }
    elif value_1 == 'value not found':
        return {
            'name': key,
            'status': 'added',
            'value': value_2
        }


def generate_children(dict_1, dict_2):
    result = []
    all_keys = sorted(list({y for x in (dict_1, dict_2) for y in list(x)}))
    for key in all_keys:
        value_1 = dict_1.get(key, 'value not found')
        value_2 = dict_2.get(key, 'value not found')
        result.append(generate_description(key, value_1, value_2))
    return result


def generate_diff_tree(dict_1, dict_2):
    result = generate_children(dict_1, dict_2)
    return {
        'status': 'root',
        'children': result
    } if result else {}
