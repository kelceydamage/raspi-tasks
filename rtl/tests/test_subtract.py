from rtl.tasks.subtract import subtract
from dummy_data import KWARGS, CONTENTS

def test_subtract():
    KWARGS = {
        'operations': [
            {
                'a': 'a',
                'b': 'b',
                'column': 'c1'
            },
            {
                'a': 'a',
                'b': 1,
                'column': 'c2'
            }
        ]
    }
    r = subtract(KWARGS, CONTENTS)
    assert r['c1'][2] == 0
    assert r['c2'][2] == 3.0
