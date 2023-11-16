diff_flat = {
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
            'value': 50,
            'value2': 20
        },
        {
            'name': 'verbose',
            'status': 'added',
            'value': True
        }
    ]
}


diff_flat_same_file = {
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

diff_empty_first = {
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


diff_empty_second = {
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


diff_both_empty = {}


diff_nested = {
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
                    'value': True,
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
                                    'value': '',
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
                    'value': 'bas',
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
                    'value': {'key': 'value'},
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
