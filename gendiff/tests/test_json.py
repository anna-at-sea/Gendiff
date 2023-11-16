from gendiff.formats.json import json_format
from gendiff.tests.fixtures.format_results import (
    json_result_flat, json_result_both_empty, json_result_nested
)
from gendiff.tests.fixtures.diff_results import (
    diff_flat, diff_both_empty, diff_nested
)
import pytest


@pytest.mark.parametrize(
    'input, expected',
    [(diff_nested, json_result_nested),
     (diff_flat, json_result_flat),
     (diff_both_empty, json_result_both_empty)
     ]
)
def test_json(input, expected):
    assert json_format(input) == expected
