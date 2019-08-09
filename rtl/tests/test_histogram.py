from rtl.tasks.histogram import histogram
from dummy_data import KWARGS, CONTENTS2

def test_histogram():
    KWARGS = {
        'operations': [
            {
                'a': 'a',
                'bins': 2,
                'column': 'c1'
            }
        ]
    }
    r = histogram(KWARGS, CONTENTS2)
    assert r['c1'][1] == 1.5