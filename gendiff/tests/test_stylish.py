# #from gendiff.stylish import stylish
# from gendiff.tests.fixtures.text_results import (
#     DIFF_FLAT, DIFF_FLAT_SAME_FILE, DIFF_EMPTY_FIRST,
#     DIFF_EMPTY_SECOND, DIFF_BOTH_EMPTY, #DIFF_NESTED,
#     STYLISH_RESULT_FLAT, STYLISH_RESULT_FLAT_SAME_FILE,
#     STYLISH_RESULT_EMPTY_FIRST, STYLISH_RESULT_EMPTY_SECOND,
#     STYLISH_RESULT_BOTH_EMPTY, STYLISH_RESULT_NESTED
# )
# import pytest


# @pytest.mark.parametrize(
#     'input, expected',
#     [(DIFF_FLAT, STYLISH_RESULT_FLAT),
#      (DIFF_FLAT_SAME_FILE, STYLISH_RESULT_FLAT_SAME_FILE),
#      (DIFF_EMPTY_FIRST, STYLISH_RESULT_EMPTY_FIRST),
#      (DIFF_EMPTY_SECOND, STYLISH_RESULT_EMPTY_SECOND),
#      (DIFF_BOTH_EMPTY, STYLISH_RESULT_BOTH_EMPTY)#,
#      #(DIFF_NESTED, STYLISH_RESULT_NESTED)
#      ]
# )
# def test_stylish(input, expected):
#     assert stylish(input) == expected