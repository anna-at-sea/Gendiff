INDENT = '    '


STATUS_PREFIXES = {
    'added': '+',
    'deleted': '-',
    'updated': '-',
    'nested': ' ',
    None: ' '
}


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
    stat = STATUS_PREFIXES[node.get('status')]
    val = node.get('old_value')
    new_val = node.get('new_value')
    lines = []
    if depth == -1:
        lines.append('{')
    elif node.get('status') == 'added':
        val = new_val
    if depth > -1:
        lines.append(
            f'{curr_indent}  {stat} {name}: {to_str(val, depth + 2)}'
        )
    if node.get('status') == 'updated':
        new_stat = STATUS_PREFIXES['added']
        lines.append(
            f'{curr_indent}  {new_stat} {name}: {to_str(new_val, depth + 2)}'
        )
    if children:
        lines.extend(
            list(map(lambda child: stylish(child, depth + 1),
                 children + ['}']))
        )
    return '\n'.join(lines)
