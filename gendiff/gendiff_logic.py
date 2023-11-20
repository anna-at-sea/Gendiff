def _values_are_dicts(value_1, value_2):
    return (isinstance(value_1, dict)
            and isinstance(value_2, dict))


def _value_changed(value_1, value_2):
    return (value_1 != 'value not found'
            and value_2 != 'value not found'
            and value_1 != value_2
            and (not isinstance(value_1, dict)
                 or not isinstance(value_2, dict)))


def generate_diff_tree(dict_1, dict_2):

    def generate_children(dict_1, dict_2):
        if not isinstance(dict_1, dict) or not isinstance(dict_2, dict):
            return []
        result = []
        all_keys = sorted(list({y for x in (dict_1, dict_2) for y in list(x)}))
        for key in all_keys:
            value_1 = dict_1.get(key, 'value not found')
            value_2 = dict_2.get(key, 'value not found')
            value = value_1
            child_1, child_2 = None, None
            if value_1 == value_2:
                status = 'unchanged'
            elif _values_are_dicts(value_1, value_2):
                status = 'unchanged'
                child_1, child_2 = value_1, value_2
                value, value_2 = 'values are dicts', 'values are dicts'
            elif _value_changed(value_1, value_2):
                status = 'changed'
            elif value_2 == 'value not found':
                status = 'deleted'
            elif value_1 == 'value not found':
                status = 'added'
                value = value_2
            result.append({
                'name': key,
                'status': status,
                'values': (value, value_2),
                'children': generate_children(child_1, child_2)
            })
        return result

    root_children = generate_children(dict_1, dict_2)
    return {
        'status': 'root',
        'values': (None, None),
        'children': root_children
    } if root_children else {}
