diff_flat = {
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
            'status': None,
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
            'status': 'updated',
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
    'values': (None, None),
    'children': [
        {
            'name': 'follow',
            'status': None,
            'values': (False, False),
            'children': []
        },
        {
            'name': 'host',
            'status': None,
            'values': ('hexlet.io', 'hexlet.io'),
            'children': []
        },
        {
            'name': 'proxy',
            'status': None,
            'values': ('123.234.53.22', '123.234.53.22'),
            'children': []
        },
        {
            'name': 'timeout',
            'status': None,
            'values': (50, 50),
            'children': []
        }
    ]
}


diff_empty_first = {
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
    'values': (None, None),
    'children': [
        {
            'name': 'common',
            'status': 'nested',
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
                    'status': None,
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
                    'status': 'updated',
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
                    'status': 'nested',
                    'values': ('values are dicts', 'values are dicts'),
                    'children': [
                        {
                            'name': 'doge',
                            'status': 'nested',
                            'values': ('values are dicts', 'values are dicts'),
                            'children': [
                                {
                                    'name': 'wow',
                                    'status': 'updated',
                                    'values': ('', 'so much'),
                                    'children': []
                                }
                            ]
                        },
                        {
                            'name': 'key',
                            'status': None,
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
            'status': 'nested',
            'values': ('values are dicts', 'values are dicts'),
            'children': [
                {
                    'name': 'baz',
                    'status': 'updated',
                    'values': ('bas', 'bars'),
                    'children': []
                },
                {
                    'name': 'foo',
                    'status': None,
                    'values': ('bar', 'bar'),
                    'children': []
                },
                {
                    'name': 'nest',
                    'status': 'updated',
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
