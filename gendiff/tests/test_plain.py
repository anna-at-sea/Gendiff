from gendiff.formats.plain import plain
from gendiff.tests.fixtures.format_results import format_result
from gendiff.tests.fixtures.diff_results import (
    diff_flat, diff_both_empty, diff_nested
)
import pytest


@pytest.mark.parametrize(
    'input, expected',
    [(diff_nested, format_result('diff_plain_nested')),
     (diff_flat, format_result('diff_plain_flat')),
     (diff_both_empty, '')
     ]
)
def test_plain(input, expected):
    assert plain(input) == expected
