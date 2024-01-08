def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def plain(node, path=''):
    if not node:
        return ''
    name = node.get('name', '')
    children = node.get('children')
    status = node.get('status')
    old_value = to_str(node.get('old_value'))
    new_value = to_str(node.get('new_value'))
    if status == 'nested':
        return '\n'.join(filter(lambda x: x is not None, list(map(
            lambda child: plain(child, path + f'{name}.'), children
        ))))
    full_path = (path + name).strip('.')
    if status == 'added':
        return f"Property '{full_path}' was added with value: {new_value}"
    if status == 'deleted':
        return f"Property '{full_path}' was removed"
    if status == 'updated':
        return f"Property '{full_path}' was updated. \
From {old_value} to {new_value}"
