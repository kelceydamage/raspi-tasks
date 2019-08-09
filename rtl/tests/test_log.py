from rtl.tasks.log import log
from dummy_data import KWARGS, CONTENTS3

def test_log():
    KWARGS = {
        'operations': [
            {
                'a': 'b',
                'column': 'c'
            }
        ]
    }
    r = log(KWARGS, CONTENTS3)
    assert r['c'][2] == 2.5649493574615367
