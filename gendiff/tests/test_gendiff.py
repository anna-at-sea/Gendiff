from gendiff import generate_diff
from gendiff.tests.fixtures.parsed_files import (
    FILE1_JSON, FILE2_JSON, EMPTY_JSON, FILE1_YAML, FILE2_YAML, EMPTY_YAML
)
from gendiff.tests.fixtures.text_results import (
    RESULT_FLAT, RESULT_FLAT_SAME_FILE,
    RESULT_EMPTY_FIRST, RESULT_EMPTY_SECOND, RESULT_BOTH_EMPTY
)
import pytest


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(FILE1_JSON, FILE2_JSON, RESULT_FLAT),
     (FILE1_JSON, FILE1_JSON, RESULT_FLAT_SAME_FILE),
     (EMPTY_JSON, FILE1_JSON, RESULT_EMPTY_FIRST),
     (FILE1_JSON, EMPTY_JSON, RESULT_EMPTY_SECOND),
     (EMPTY_JSON, EMPTY_JSON, RESULT_BOTH_EMPTY)
     ]
)
def test_gendiff_flat_json(input_1, input_2, expected):
    assert generate_diff(input_1, input_2) == expected


@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [(FILE1_YAML, FILE2_YAML, RESULT_FLAT),
     (FILE1_YAML, FILE1_YAML, RESULT_FLAT_SAME_FILE),
     (EMPTY_YAML, FILE1_YAML, RESULT_EMPTY_FIRST),
     (FILE1_YAML, EMPTY_YAML, RESULT_EMPTY_SECOND),
     (EMPTY_YAML, EMPTY_YAML, RESULT_BOTH_EMPTY)
     ]
)
def test_gendiff_flat_yaml(input_1, input_2, expected):
    assert generate_diff(input_1, input_2) == expected
