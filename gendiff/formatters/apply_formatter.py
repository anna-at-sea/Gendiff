from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_formatter import json_formatter


def apply_formatter(formatter_name):
    formatters = {'stylish': stylish, 'plain': plain, 'json': json_formatter}
    return formatters[formatter_name]
