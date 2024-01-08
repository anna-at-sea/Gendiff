INDENT = '    '


STATUS_PREFIXES = {
    'added': '+',
    'deleted': '-',
    'updated': '-',
    'nested': ' ',
    'unchanged': ' '
}


def to_str(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif not isinstance(value, dict):
        return str(value)
    lines = []
    for key, val in value.items():
        lines.append(
            f'{INDENT * depth}{key}: {to_str(val, depth + 1)}'
        )
    result = ['{'] + lines + [f'{INDENT * (depth - 1)}' + '}']
    return '\n'.join(result)


def stylish(node, depth=-1):
    if not node:
        return '{\n\n}'
    name = node.get('name')
    stat = STATUS_PREFIXES[node.get('status')]
    val = node.get('old_value')
    new_val = node.get('new_value')
    lines = []
    if node.get('status') == 'added':
        val = new_val
    if node.get('status') in ['added', 'deleted', 'updated', 'unchanged']:
        lines.append(
            f'{INDENT * depth}  {stat} {name}: {to_str(val, depth + 2)}'
        )
    if node.get('status') == 'updated':
        new_stat = STATUS_PREFIXES['added']
        lines.append(
            f'{INDENT * depth}  {new_stat} {name}: {to_str(new_val, depth + 2)}'
        )
    if node.get('status') == 'nested':
        if name:
            lines.append(f'{INDENT * depth}  {stat} {name}: ' + '{')
        elif not name:
            lines.append('{')
        lines.extend(
            list(map(lambda child: stylish(child, depth + 1),
                 node.get('children')))
        )
        lines.append(f'{INDENT * (depth + 1)}' + '}')
    return '\n'.join(lines)
