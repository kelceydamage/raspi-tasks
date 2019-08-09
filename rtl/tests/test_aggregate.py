from rtl.tasks.aggregate import aggregate
from dummy_data import KWARGS, CONTENTS3

def test_aggregate():
    KWARGS = {
        'operations': [
            {
                'column': 'c',
                'columns': [
                    'a',
                    'b'
                ]
            }
        ]
    }
    r = aggregate(KWARGS, CONTENTS3)
    assert r['c'][2] == 7.5