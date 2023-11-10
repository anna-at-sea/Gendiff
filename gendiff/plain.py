from gendiff.gendiff_logic import (
    get_children, get_value1, get_value2,
    get_status, get_name
)


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


def convert_to_plain(value):
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


def build_lines(node, acc):
    name = get_name(node)
    children = get_children(node)
    stat = get_status(node)
    val1 = convert_to_plain(get_value1(node))
    val2 = convert_to_plain(get_value2(node))
    if children and name:
        acc += f'{name}.'
    if children:
        return list(map(lambda child: build_lines(child, acc), children))
    elif stat == 'added':
        return f"Property '{acc + name}' was added with value: {val1}"
    elif stat == 'deleted':
        return f"Property '{acc + name}' was removed"
    elif stat == 'changed':
        return f"Property '{acc + name}' was updated. From {val1} to {val2}"


def plain(tree):
    if not tree:
        return ''
    flat_lines = flatten(build_lines(tree, ''))
    return '\n'.join(filter(lambda x: x is not None, flat_lines))
