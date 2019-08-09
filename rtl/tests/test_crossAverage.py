from rtl.tasks.crossAverage import crossAverage
from dummy_data import KWARGS, CONTENTS3

def test_crossAverage():
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
    r = crossAverage(KWARGS, CONTENTS3)
    assert r['c'][2] == 7.5
