from gendiff.formats.stylish import stylish
from gendiff.tests.fixtures.format_results import (
    stylish_result_flat, stylish_result_flat_same_file,
    stylish_result_empty_first, stylish_result_empty_second,
    stylish_result_both_empty, stylish_result_nested
)
from gendiff.tests.fixtures.diff_results import (
    diff_flat, diff_flat_same_file, diff_empty_first,
    diff_empty_second, diff_both_empty, diff_nested
)
import pytest


@pytest.mark.parametrize(
    'input, expected',
    [(diff_flat, stylish_result_flat),
     (diff_flat_same_file, stylish_result_flat_same_file),
     (diff_empty_first, stylish_result_empty_first),
     (diff_empty_second, stylish_result_empty_second),
     (diff_both_empty, stylish_result_both_empty),
     (diff_nested, stylish_result_nested)
     ]
)
def test_stylish(input, expected):
    assert stylish(input) == expected
