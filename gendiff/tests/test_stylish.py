from gendiff.formats.stylish import stylish
from gendiff.tests.fixtures.format_results import format_result
from gendiff.tests.fixtures.diff_results import (
    diff_flat, diff_flat_same_file, diff_empty_first,
    diff_empty_second, diff_both_empty, diff_nested
)
import pytest


@pytest.mark.parametrize(
    'input, expected',
    [(diff_flat, format_result('diff_file1_file2')),
     (diff_flat_same_file, format_result('diff_file1_file1')),
     (diff_empty_first, format_result('diff_empty_file1')),
     (diff_empty_second, format_result('diff_file1_empty')),
     (diff_both_empty, '{\n\n}'),
     (diff_nested, format_result('diff_nested'))
     ]
)
def test_stylish(input, expected):
    assert stylish(input) == expected
