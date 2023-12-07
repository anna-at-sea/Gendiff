from gendiff.gendiff_tree_builder import generate_diff_tree
from gendiff.content import get_content
from gendiff.formatters.apply_formatter import apply_formatter


def generate_diff(first_file, second_file, formatter='stylish'):
    return apply_formatter(formatter)(generate_diff_tree(
        get_content(first_file), get_content(second_file)
    ))
