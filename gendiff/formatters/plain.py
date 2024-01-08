def flatten(list_of_lists):
    result = []
    for item in list_of_lists:
        item = item if isinstance(item, list) else [item]
        result.extend(item)
    if any(isinstance(i, list) for i in result):
        return flatten(result)
    return result


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return "'" + value + "'"
    else:
        return value


def plain(node, acc=''):
    if not node:
        return ''
    name = node.get('name', '')
    children = node.get('children')
    status = node.get('status')
    old_value = to_str(node.get('old_value'))
    new_value = to_str(node.get('new_value'))
    if status == 'nested':
        return '\n'.join(filter(lambda x: x is not None, flatten(
            list(map(lambda child: plain(child, acc + f'{name}.'), children))
        )))
    full_name = (acc + name).strip('.')
    if status == 'added':
        return f"Property '{full_name}' was added with value: {new_value}"
    if status == 'deleted':
        return f"Property '{full_name}' was removed"
    if status == 'updated':
        return f"Property '{full_name}' was updated. \
From {old_value} to {new_value}"
