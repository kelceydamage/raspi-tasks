from rtl.tasks.difference import difference
from dummy_data import KWARGS, CONTENTS2

def test_difference():
    KWARGS = {
        'operations': [
            {
                'a': 'a',
                'b': 'b',
                'column': 'c'
            }
        ]
    }
    r = difference(KWARGS, CONTENTS2)
    assert r['a'][2] == 2
