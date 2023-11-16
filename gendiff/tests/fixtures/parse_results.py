parse_result_flat = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False
}


parse_result_nested = {
    'common': {
        'follow': False,
        'setting1': 'Value 1',
        'setting3': None,
        'setting4': 'blah blah',
        'setting5': {
            'key5': 'value5'
        },
        'setting6': {
            'key': 'value',
            'ops': 'vops',
            'doge': {
                'wow': 'so much'
            }
        }
    },
    'group1': {
        'foo': 'bar',
        'baz': 'bars',
        'nest': 'str'
    },
    'group3': {
        'deep': {
            'id': {
                'number': 45
            }
        },
        'fee': 100500
    }
}
