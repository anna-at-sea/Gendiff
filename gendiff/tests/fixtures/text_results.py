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
    'status': 'root',
    'children': [
        {
            'name': 'follow',
            'status': 'deleted',
            'value': False
        },
        {
            'name': 'host',
            'status': 'unchanged',
            'value': 'hexlet.io'
        },
        {
            'name': 'proxy',
            'status': 'deleted',
            'value': '123.234.53.22'
        },
        {
            'name': 'timeout',
            'status': 'changed',
            'value1': 50,
            'value2': 20
        },
        {
            'name': 'verbose',
            'status': 'added',
            'value': True
        }
    ]
}


DIFF_FLAT_SAME_FILE = {
    'status': 'root',
    'children': [
        {
            'name': 'follow',
            'status': 'unchanged',
            'value': False
        },
        {
            'name': 'host',
            'status': 'unchanged',
            'value': 'hexlet.io'
        },
        {
            'name': 'proxy',
            'status': 'unchanged',
            'value': '123.234.53.22'
        },
        {
            'name': 'timeout',
            'status': 'unchanged',
            'value': 50
        }
    ]
}

DIFF_EMPTY_FIRST = {
    'status': 'root',
    'children': [
        {
            'name': 'follow',
            'status': 'added',
            'value': False
        },
        {
            'name': 'host',
            'status': 'added',
            'value': 'hexlet.io'
        },
        {
            'name': 'proxy',
            'status': 'added',
            'value': '123.234.53.22'
        },
        {
            'name': 'timeout',
            'status': 'added',
            'value': 50
        }
    ]
}


DIFF_EMPTY_SECOND = {
    'status': 'root',
    'children': [
        {
            'name': 'follow',
            'status': 'deleted',
            'value': False
        },
        {
            'name': 'host',
            'status': 'deleted',
            'value': 'hexlet.io'
        },
        {
            'name': 'proxy',
            'status': 'deleted',
            'value': '123.234.53.22'
        },
        {
            'name': 'timeout',
            'status': 'deleted',
            'value': 50
        }
    ]
}


DIFF_BOTH_EMPTY = {}


DIFF_NESTED = {
    'status': 'root',
    'children': [
        {
            'name': 'common',
            'status': 'unchanged',
            'children': [
                {
                    'name': 'follow',
                    'status': 'added',
                    'value': False
                },
                {
                    'name': 'setting1',
                    'status': 'unchanged',
                    'value': 'Value 1'
                },
                {
                    'name': 'setting2',
                    'status': 'deleted',
                    'value': 200
                },
                {
                    'name': 'setting3',
                    'status': 'changed',
                    'value1': True,
                    'value2': None
                },
                {
                    'name': 'setting4',
                    'status': 'added',
                    'value': 'blah blah'
                },
                {
                    'name': 'setting5',
                    'status': 'added',
                    'value': {'key5': 'value5'}
                },
                {
                    'name': 'setting6',
                    'status': 'unchanged',
                    'children': [
                        {
                            'name': 'doge',
                            'status': 'unchanged',
                            'children': [
                                {
                                    'name': 'wow',
                                    'status': 'changed',
                                    'value1': '',
                                    'value2': 'so much'
                                }
                            ]
                        },
                        {
                            'name': 'key',
                            'status': 'unchanged',
                            'value': 'value'
                        },
                        {
                            'name': 'ops',
                            'status': 'added',
                            'value': 'vops'
                        }
                    ]
                }
            ]
        },
        {
            'name': 'group1',
            'status': 'unchanged',
            'children': [
                {
                    'name': 'baz',
                    'status': 'changed',
                    'value1': 'bas',
                    'value2': 'bars'
                },
                {
                    'name': 'foo',
                    'status': 'unchanged',
                    'value': 'bar'
                },
                {
                    'name': 'nest',
                    'status': 'changed',
                    'value1': {'key': 'value'},
                    'value2': 'str'
                }
            ]
        },
        {
            'name': 'group2',
            'status': 'deleted',
            'value': {'abc': 12345, 'deep': {'id': 45}}
        },
        {
            'name': 'group3',
            'status': 'added',
            'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}
        }
    ]
}
