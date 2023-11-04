from gendiff.gendiff_logic import (
    get_children, get_value1, get_value2, get_status, get_name
)


def stylish(tree):  # noqa C901
    def walk(node, depth):
        if node == '}':
            return ('    ' * depth) + node
        name = get_name(node)
        children = get_children(node)
        status = get_status(node)
        value1 = get_value1(node)
        value2 = get_value2(node)
        lines = []
        if status == 'unchanged' and not children:
            return ('    ' * depth) + f'    {name}: {value1}'
        elif status == 'added':
            return ('    ' * depth) + f'  + {name}: {value1}'
        elif status == 'deleted':
            return ('    ' * depth) + f'  - {name}: {value1}'
        elif status == 'changed':
            return (('    ' * depth) + f'  - {name}: {value1}\n'
                    + ('    ' * depth) + f'  + {name}: {value2}')
        elif children:
            if status != 'root':
                lines.append(('    ' * depth) + f'    {name}: ' + '{')
            for child in children + ['}']:
                lines.append(walk(child, depth + 1))
        return '\n'.join(lines)
    return '{\n' + walk(tree, -1) + '\n}'
