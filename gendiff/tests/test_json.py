from gendiff.formats.json import json_format
from gendiff.tests.fixtures.format_results import format_result
from gendiff.tests.fixtures.diff_results import (
    diff_flat, diff_both_empty, diff_nested
)
import pytest


@pytest.mark.parametrize(
    'input, expected',
    [(diff_nested, format_result('diff_json_nested')),
     (diff_flat, format_result('diff_json_flat')),
     (diff_both_empty, '{}')
     ]
)
def test_json(input, expected):
    assert json_format(input) == expected
