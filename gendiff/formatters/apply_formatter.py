from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_formatter import json_formatter


def apply_formatter(formatter_name, content):
    if formatter_name == 'stylish':
        return stylish(content)
    elif formatter_name == 'plain':
        return plain(content)
    elif formatter_name == 'json':
        return json_formatter(content)
    else:
        raise ValueError(f'\'{formatter_name}\' format is not supported')
