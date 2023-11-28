def flatten(list_of_lists):
    result = []

    def walk(item):
        if not isinstance(item, list):
            result.append(item)
            return
        for i in item:
            walk(i)

    walk(list_of_lists)
    return result


def to_str(value):
    if isinstance(value, bool):
        new_value = str(value).lower()
    elif value is None:
        new_value = 'null'
    elif isinstance(value, dict):
        new_value = '[complex value]'
    elif isinstance(value, str):
        new_value = "'" + value + "'"
    else:
        new_value = value
    return new_value


def plain(node, acc=''):
    if not node:
        return ''
    name = node.get('name', '')
    children = node.get('children')
    stat = node.get('status')
    val1 = to_str(node.get('values')[0])
    val2 = to_str(node.get('values')[1])
    if stat == 'nested':
        acc += f'{name}.'
    if children:
        child_list = list(map(lambda child: plain(child, acc), children))
        return '\n'.join(filter(lambda x: x is not None, flatten(child_list)))
    elif stat == 'added':
        return f"Property '{acc + name}' was added with value: {val1}"
    elif stat == 'deleted':
        return f"Property '{acc + name}' was removed"
    elif stat == 'updated':
        return f"Property '{acc + name}' was updated. From {val1} to {val2}"