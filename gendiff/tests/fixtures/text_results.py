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
    STYLISH_RESULT_FLAT = diff_file1_file2.read()
    STYLISH_RESULT_FLAT_SAME_FILE = diff_file1_file1.read()
    STYLISH_RESULT_EMPTY_FIRST = diff_empty_file1.read()
    STYLISH_RESULT_EMPTY_SECOND = diff_file1_empty.read()
    STYLISH_RESULT_NESTED = diff_nested.read()
STYLISH_RESULT_BOTH_EMPTY = '{\n\n}'


DIFF_FLAT = {
    'host': {
        'status': 'unchanged',
        'value': 'hexlet.io'
    },
    'timeout': {
        'status': 'changed',
        'value1': '50',
        'value2': '20'
    },
    'proxy': {
        'status': 'deleted',
        'value': '123.234.53.22'
    },
    'follow': {
        'status': 'deleted',
        'value': 'false'
    },
    'verbose': {
        'status': 'added',
        'value': 'true'
    }
}


DIFF_FLAT_SAME_FILE = {
    'host': {
        'status': 'unchanged',
        'value': 'hexlet.io'
    },
    'timeout': {
        'status': 'unchanged',
        'value': '50'
    },
    'proxy': {
        'status': 'unchanged',
        'value': '123.234.53.22'
    },
    'follow': {
        'status': 'unchanged',
        'value': 'false'
    }
}


DIFF_EMPTY_FIRST = {
    'host': {
        'status': 'added',
        'value': 'hexlet.io'
    },
    'timeout': {
        'status': 'added',
        'value': '50'
    },
    'proxy': {
        'status': 'added',
        'value': '123.234.53.22'
    },
    'follow': {
        'status': 'added',
        'value': 'false'
    }
}


DIFF_EMPTY_SECOND = {
    'host': {
        'status': 'deleted',
        'value': 'hexlet.io'
    },
    'timeout': {
        'status': 'deleted',
        'value': '50'
    },
    'proxy': {
        'status': 'deleted',
        'value': '123.234.53.22'
    },
    'follow': {
        'status': 'deleted',
        'value': 'false'
    }
}


DIFF_BOTH_EMPTY = {}


DIFF_NESTED = {
    'common': {
        'status': 'unchanged',
        'children': {
            'follow': {
                'status': 'added',
                'value': 'false'
            },
            'setting1': {
                'status': 'unchanged',
                'value': 'Value 1'
            },
            'setting2': {
                'status': 'deleted',
                'value': '200'
            },
            'setting3': {
                'status': 'changed',
                'value1': 'true',
                'value2': 'null'
            },
            'setting4': {
                'status': 'added',
                'value': 'blah blah'
            },
            'setting5': {
                'status': 'added',
                'value': {'key5': 'value5'}
            },
            'setting6': {
                'status': 'unchanged',
                'children': {
                    'doge': {
                        'status': 'unchanged',
                        'children': {
                            'wow': {
                                'status': 'changed',
                                'value1': '',
                                'value2': 'so much'
                            }
                        }
                    },
                    'key': {
                        'status': 'unchanged',
                        'value': 'value'
                    },
                    'ops': {
                        'status': 'added',
                        'value': 'vops'
                    }
                }
            }
        }
    },
    'group1': {
        'status': 'unchanged',
        'children': {
            'baz': {
                'status': 'changed',
                'value1': 'bas',
                'value2': 'bars'
            },
            'foo': {
                'status': 'unchanged',
                'value': 'bar'
            },
            'nest': {
                'status': 'changed',
                'value1': {'key': 'value'},
                'value2': 'str'
            }
        }
    },
    'group2': {
        'status': 'deleted',
        'value': {'abc': '12345', 'deep': {'id': '45'}}
    },
    'group3': {
        'status': 'added',
        'value': {'deep': {'id': {'number': '45'}}, 'fee': '100500'}
    }
}
