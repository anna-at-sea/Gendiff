from gendiff.formats.plain import plain
from gendiff.tests.fixtures.format_results import (
    plain_result_flat, plain_result_both_empty, plain_result_nested
)
from gendiff.tests.fixtures.diff_results import (
    diff_flat, diff_both_empty, diff_nested
)
import pytest


@pytest.mark.parametrize(
    'input, expected',
    [(diff_nested, plain_result_nested),
     (diff_flat, plain_result_flat),
     (diff_both_empty, plain_result_both_empty)
     ]
)
def test_plain(input, expected):
    assert plain(input) == expected
