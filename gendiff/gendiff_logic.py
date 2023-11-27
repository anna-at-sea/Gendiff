def generate_children(dict_1, dict_2):
    result = []
    all_keys = sorted(dict_1.keys() | dict_2.keys())
    deleted_keys = dict_1.keys() - dict_2.keys()
    added_keys = dict_2.keys() - dict_1.keys()
    for key in all_keys:
        value_1 = dict_1.get(key, 'value not found')
        value_2 = dict_2.get(key, 'value not found')
        value = value_1
        child_1, child_2 = {}, {}
        status = None
        if (isinstance(value_1, dict) and isinstance(value_2, dict)):
            status = 'nested'
            child_1, child_2 = value_1, value_2
            value, value_2 = 'values are dicts', 'values are dicts'
        elif key in deleted_keys:
            status = 'deleted'
        elif key in added_keys:
            status = 'added'
            value = value_2
        elif value_1 != value_2:
            status = 'updated'
        result.append({
            'name': key,
            'status': status,
            'values': (value, value_2),
            'children': generate_children(child_1, child_2)
        })
    return result


def generate_diff_tree(dict_1, dict_2):
    root_children = generate_children(dict_1, dict_2)
    return {
        'values': (None, None),
        'children': root_children
    } if root_children else {}
