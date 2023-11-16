with (open('gendiff/tests/fixtures/txt/diff_file1_file2.txt', 'r')
      as diff_file1_file2,
      open('gendiff/tests/fixtures/txt/diff_file1_file1.txt', 'r')
      as diff_file1_file1,
      open('gendiff/tests/fixtures/txt/diff_empty_file1.txt', 'r')
      as diff_empty_file1,
      open('gendiff/tests/fixtures/txt/diff_file1_empty.txt', 'r')
      as diff_file1_empty,
      open('gendiff/tests/fixtures/txt/diff_nested.txt', 'r')
      as diff_nested):
    stylish_result_flat = diff_file1_file2.read()
    stylish_result_flat_same_file = diff_file1_file1.read()
    stylish_result_empty_first = diff_empty_file1.read()
    stylish_result_empty_second = diff_file1_empty.read()
    stylish_result_nested = diff_nested.read()


with (open('gendiff/tests/fixtures/txt/diff_plain_nested.txt', 'r')
      as diff_plain_nested,
      open('gendiff/tests/fixtures/txt/diff_plain_flat.txt', 'r')
      as diff_plain_flat):
    plain_result_nested = diff_plain_nested.read()
    plain_result_flat = diff_plain_flat.read()


with (open('gendiff/tests/fixtures/txt/diff_json_nested.txt', 'r')
      as diff_json_nested,
      open('gendiff/tests/fixtures/txt/diff_json_flat.txt', 'r')
      as diff_json_flat):
    json_result_nested = diff_json_nested.read()
    json_result_flat = diff_json_flat.read()


stylish_result_both_empty = '{\n\n}'
plain_result_both_empty = ''
json_result_both_empty = '{}'
