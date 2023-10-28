with (open('gendiff/tests/fixtures/txt/diff_file1_file2.txt', 'r')
      as diff_file1_file2,
      open('gendiff/tests/fixtures/txt/diff_file1_file1.txt', 'r')
      as diff_file1_file1,
      open('gendiff/tests/fixtures/txt/diff_empty_file1.txt', 'r')
      as diff_empty_file1,
      open('gendiff/tests/fixtures/txt/diff_file1_empty.txt', 'r')
      as diff_file1_empty):
    RESULT_FLAT = diff_file1_file2.read()
    RESULT_FLAT_SAME_FILE = diff_file1_file1.read()
    RESULT_EMPTY_FIRST = diff_empty_file1.read()
    RESULT_EMPTY_SECOND = diff_file1_empty.read()
RESULT_BOTH_EMPTY = '{\n\n}'
