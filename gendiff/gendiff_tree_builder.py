def generate_diff_tree(dict_1, dict_2, depth=0):
    if depth == 0:
        return {
            'children': generate_diff_tree(dict_1, dict_2, 1)
        } if dict_1 or dict_2 else {}
    result = []
    all_keys = sorted(dict_1.keys() | dict_2.keys())
    deleted_keys = dict_1.keys() - dict_2.keys()
    added_keys = dict_2.keys() - dict_1.keys()
    for key in all_keys:
        old_value = dict_1.get(key, 'value not found')
        new_value = dict_2.get(key, 'value not found')
        children = ({}, {})
        status = None
        if (isinstance(old_value, dict) and isinstance(new_value, dict)):
            status = 'nested'
            children = old_value, new_value
            old_value, new_value = 'values are dicts', 'values are dicts'
        elif key in deleted_keys:
            status = 'deleted'
        elif key in added_keys:
            status = 'added'
        elif old_value != new_value:
            status = 'updated'
        result.append({
            'name': key,
            'status': status,
            'old_value': old_value,
            'new_value': new_value,
            'children': generate_diff_tree(*children, 1)
        })
    return result
