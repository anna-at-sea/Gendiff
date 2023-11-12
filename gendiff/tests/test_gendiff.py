from gendiff import generate_diff_tree
from gendiff.tests.fixtures.parsed_files import (
    FILE1_JSON, FILE2_JSON, EMPTY_JSON, FILE1_YAML, FILE2_YAML, EMPTY_YAML,
    NESTED_FILE1_JSON, NESTED_FILE2_JSON,
    NESTED_FILE1_YAML, NESTED_FILE2_YAML
)
from gendiff.tests.fixtures.text_results import (
    DIFF_FLAT, DIFF_FLAT_SAME_FILE, DIFF_EMPTY_FIRST,
    DIFF_EMPTY_SECOND, DIFF_BOTH_EMPTY, DIFF_NESTED
)
import pytest


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(FILE1_JSON, FILE2_JSON, DIFF_FLAT),
     (FILE1_JSON, FILE1_JSON, DIFF_FLAT_SAME_FILE),
     (EMPTY_JSON, FILE1_JSON, DIFF_EMPTY_FIRST),
     (FILE1_JSON, EMPTY_JSON, DIFF_EMPTY_SECOND),
     (EMPTY_JSON, EMPTY_JSON, DIFF_BOTH_EMPTY)
     ]
)
def test_gendiff_flat_json(input_1, input_2, expected):
    assert generate_diff_tree(input_1, input_2) == expected


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(FILE1_YAML, FILE2_YAML, DIFF_FLAT),
     (FILE1_YAML, FILE1_YAML, DIFF_FLAT_SAME_FILE),
     (EMPTY_YAML, FILE1_YAML, DIFF_EMPTY_FIRST),
     (FILE1_YAML, EMPTY_YAML, DIFF_EMPTY_SECOND),
     (EMPTY_YAML, EMPTY_YAML, DIFF_BOTH_EMPTY)
     ]
)
def test_gendiff_flat_yaml(input_1, input_2, expected):
    assert generate_diff_tree(input_1, input_2) == expected


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(NESTED_FILE1_JSON, NESTED_FILE2_JSON, DIFF_NESTED),
     (NESTED_FILE1_YAML, NESTED_FILE2_YAML, DIFF_NESTED)
     ]
)
def test_gendiff_nested(input_1, input_2, expected):
    assert generate_diff_tree(input_1, input_2) == expected
