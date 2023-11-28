INDENT = '    '
ADDED = '+'
DELETED = '-'
UNCHANGED = ' '


def stylish_status1(node):
    status = node.get('status')
    if status in (None, 'nested'):
        return UNCHANGED
    elif status == 'added':
        return ADDED
    elif status == 'deleted':
        return DELETED
    elif status == 'updated':
        return DELETED


def stylish_status2(node):
    if node.get('status') == 'updated':
        return ADDED


def to_str(value, stylish_depth):

    def walk(node, depth):
        if isinstance(node, bool):
            return str(node).lower()
        elif node is None:
            return 'null'
        elif node == 'values are dicts':
            return '{'
        elif not isinstance(node, dict):
            return str(node)
        total_depth = depth + stylish_depth
        lines = []
        for key, val in node.items():
            lines.append(
                f'{INDENT * total_depth}{key}: {walk(val, depth + 1)}'
            )
        result = ['{'] + lines + [f'{INDENT * (total_depth - 1)}' + '}']
        return '\n'.join(result)

    return walk(value, 0)


def stylish(node, depth=-1):
    if not node:
        return '{\n\n}'
    curr_indent = INDENT * depth
    if node == '}':
        return curr_indent + node
    name = node.get('name')
    children = node.get('children')
    stat1 = stylish_status1(node)
    val1 = node.get('values')[0]
    lines = []
    if depth == -1:
        lines.append('{')
    elif depth > -1:
        lines.append(
            f'{curr_indent}  {stat1} {name}: {to_str(val1, depth + 2)}'
        )
    if node.get('status') == 'updated':
        stat2 = stylish_status2(node)
        val2 = node.get('values')[1]
        lines.append(
            f'{curr_indent}  {stat2} {name}: {to_str(val2, depth + 2)}'
        )
    if children:
        lines.extend(
            list(map(lambda child: stylish(child, depth + 1),
                 children + ['}']))
        )
    return '\n'.join(lines)
