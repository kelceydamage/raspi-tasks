from rtl.tasks.filterRows import filterRows
from dummy_data import KWARGS, CONTENTS2

def test_filterRows():
    KWARGS = {
        'operations': [
            {
            'column': 'a',
            'value': 2,
            'method': 'eq'
            },
            {
            'column': 'a',
            'value': 2,
            'method': 'ne'
            },
        ]
    }
    r = filterRows(KWARGS, CONTENTS2)
    KWARGS = {
        'operations': [
            {
            'column': 'a',
            'value': 2,
            'method': 'lt'
            },
            {
            'column': 'a',
            'value': 2,
            'method': 'le'
            },
        ]
    }
    r = filterRows(KWARGS, CONTENTS2)
    KWARGS = {
        'operations': [
            {
            'column': 'a',
            'value': 2,
            'method': 'gt'
            },
            {
            'column': 'a',
            'value': 2,
            'method': 'ge'
            }
        ]
    }
    r = filterRows(KWARGS, CONTENTS2)
    assert r['a'][0] == 0
