from gendiff.plain import plain
from gendiff.tests.fixtures.text_results import (
    DIFF_FLAT, PLAIN_RESULT_FLAT,
    DIFF_BOTH_EMPTY, PLAIN_RESULT_BOTH_EMPTY,
    DIFF_NESTED, PLAIN_RESULT_NESTED
)
import pytest


@pytest.mark.parametrize(
    'input, expected',
    [(DIFF_NESTED, PLAIN_RESULT_NESTED),
     (DIFF_FLAT, PLAIN_RESULT_FLAT),
     (DIFF_BOTH_EMPTY, PLAIN_RESULT_BOTH_EMPTY)
     ]
)
def test_plain(input, expected):
    assert plain(input) == expected
