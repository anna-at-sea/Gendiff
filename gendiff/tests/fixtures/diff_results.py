diff_flat = {
    'status': 'root',
    'values': (None, None),
    'children': [
        {
            'name': 'follow',
            'status': 'deleted',
            'values': (False, 'value not found'),
            'children': []
        },
        {
            'name': 'host',
            'status': 'unchanged',
            'values': ('hexlet.io', 'hexlet.io'),
            'children': []
        },
        {
            'name': 'proxy',
            'status': 'deleted',
            'values': ('123.234.53.22', 'value not found'),
            'children': []
        },
        {
            'name': 'timeout',
            'status': 'changed',
            'values': (50, 20),
            'children': []
        },
        {
            'name': 'verbose',
            'status': 'added',
            'values': (True, True),
            'children': []
        }
    ]
}


diff_flat_same_file = {
    'status': 'root',
    'values': (None, None),
    'children': [
        {
            'name': 'follow',
            'status': 'unchanged',
            'values': (False, False),
            'children': []
        },
        {
            'name': 'host',
            'status': 'unchanged',
            'values': ('hexlet.io', 'hexlet.io'),
            'children': []
        },
        {
            'name': 'proxy',
            'status': 'unchanged',
            'values': ('123.234.53.22', '123.234.53.22'),
            'children': []
        },
        {
            'name': 'timeout',
            'status': 'unchanged',
            'values': (50, 50),
            'children': []
        }
    ]
}


diff_empty_first = {
    'status': 'root',
    'values': (None, None),
    'children': [
        {
            'name': 'follow',
            'status': 'added',
            'values': (False, False),
            'children': []
        },
        {
            'name': 'host',
            'status': 'added',
            'values': ('hexlet.io', 'hexlet.io'),
            'children': []
        },
        {
            'name': 'proxy',
            'status': 'added',
            'values': ('123.234.53.22', '123.234.53.22'),
            'children': []
        },
        {
            'name': 'timeout',
            'status': 'added',
            'values': (50, 50),
            'children': []
        }
    ]
}


diff_empty_second = {
    'status': 'root',
    'values': (None, None),
    'children': [
        {
            'name': 'follow',
            'status': 'deleted',
            'values': (False, 'value not found'),
            'children': []
        },
        {
            'name': 'host',
            'status': 'deleted',
            'values': ('hexlet.io', 'value not found'),
            'children': []
        },
        {
            'name': 'proxy',
            'status': 'deleted',
            'values': ('123.234.53.22', 'value not found'),
            'children': []
        },
        {
            'name': 'timeout',
            'status': 'deleted',
            'values': (50, 'value not found'),
            'children': []
        }
    ]
}


diff_both_empty = {}


diff_nested = {
    'status': 'root',
    'values': (None, None),
    'children': [
        {
            'name': 'common',
            'status': 'unchanged',
            'values': ('values are dicts', 'values are dicts'),
            'children': [
                {
                    'name': 'follow',
                    'status': 'added',
                    'values': (False, False),
                    'children': []
                },
                {
                    'name': 'setting1',
                    'status': 'unchanged',
                    'values': ('Value 1', 'Value 1'),
                    'children': []
                },
                {
                    'name': 'setting2',
                    'status': 'deleted',
                    'values': (200, 'value not found'),
                    'children': []
                },
                {
                    'name': 'setting3',
                    'status': 'changed',
                    'values': (True, None),
                    'children': []
                },
                {
                    'name': 'setting4',
                    'status': 'added',
                    'values': ('blah blah', 'blah blah'),
                    'children': []
                },
                {
                    'name': 'setting5',
                    'status': 'added',
                    'values': ({'key5': 'value5'}, {'key5': 'value5'}),
                    'children': []
                },
                {
                    'name': 'setting6',
                    'status': 'unchanged',
                    'values': ('values are dicts', 'values are dicts'),
                    'children': [
                        {
                            'name': 'doge',
                            'status': 'unchanged',
                            'values': ('values are dicts', 'values are dicts'),
                            'children': [
                                {
                                    'name': 'wow',
                                    'status': 'changed',
                                    'values': ('', 'so much'),
                                    'children': []
                                }
                            ]
                        },
                        {
                            'name': 'key',
                            'status': 'unchanged',
                            'values': ('value', 'value'),
                            'children': []
                        },
                        {
                            'name': 'ops',
                            'status': 'added',
                            'values': ('vops', 'vops'),
                            'children': []
                        }
                    ]
                }
            ]
        },
        {
            'name': 'group1',
            'status': 'unchanged',
            'values': ('values are dicts', 'values are dicts'),
            'children': [
                {
                    'name': 'baz',
                    'status': 'changed',
                    'values': ('bas', 'bars'),
                    'children': []
                },
                {
                    'name': 'foo',
                    'status': 'unchanged',
                    'values': ('bar', 'bar'),
                    'children': []
                },
                {
                    'name': 'nest',
                    'status': 'changed',
                    'values': ({'key': 'value'}, 'str'),
                    'children': []
                }
            ]
        },
        {
            'name': 'group2',
            'status': 'deleted',
            'values': ({'abc': 12345, 'deep': {'id': 45}}, 'value not found'),
            'children': []
        },
        {
            'name': 'group3',
            'status': 'added',
            'values': ({'deep': {'id': {'number': 45}}, 'fee': 100500},
                       {'deep': {'id': {'number': 45}}, 'fee': 100500}),
            'children': []
        }
    ]
}
