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
            'children': generate_diff_no_root(value_1, value_2)
        }
    elif _value_changed(value_1, value_2):
        return {
            'name': key,
            'status': 'changed',
            'value1': value_1,
            'value2': value_2
        }
    elif _value_deleted(value_1, value_2):
        return {
            'name': key,
            'status': 'deleted',
            'value': value_1
        }
    elif _value_added(value_1, value_2):
        return {
            'name': key,
            'status': 'added',
            'value': value_2
        }


def generate_diff_no_root(dict_1, dict_2):
    result = []
    all_keys = get_all_keys(dict_1, dict_2)
    for key in all_keys:
        value_1 = dict_1.get(key)
        value_2 = dict_2.get(key)
        result.append(generate_description(key, value_1, value_2))
    return result


def generate_diff(dict_1, dict_2):
    result = generate_diff_no_root(dict_1, dict_2)
    return {
        'status': 'root',
        'children': result
    } if result else {}


def get_children(node):
    return node.get('children')


def get_value1(node):
    value = node.get('value')
    value1 = node.get('value1')
    return value if value else value1


def get_value2(node):
    return node.get('value2')


def get_status(node):
    return node.get('status')


def get_name(node):
    return node.get('name')
