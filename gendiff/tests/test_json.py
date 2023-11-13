from gendiff.formats.json import json_format
from gendiff.tests.fixtures.text_results import (
    DIFF_FLAT, JSON_RESULT_FLAT,
    DIFF_BOTH_EMPTY, JSON_RESULT_BOTH_EMPTY,
    DIFF_NESTED, JSON_RESULT_NESTED
)
import pytest


@pytest.mark.parametrize(
    'input, expected',
    [(DIFF_NESTED, JSON_RESULT_NESTED),
     (DIFF_FLAT, JSON_RESULT_FLAT),
     (DIFF_BOTH_EMPTY, JSON_RESULT_BOTH_EMPTY)
     ]
)
def test_plain(input, expected):
    assert json_format(input) == expected
