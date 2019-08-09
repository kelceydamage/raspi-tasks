from rtl.tasks.divide import divide
from dummy_data import KWARGS, CONTENTS

def test_divide():
    KWARGS = {
        'operations': [
            {
                'a': 'a',
                'b': 'b',
                'column': 'c1'
            },
             {
                'a': 'a',
                'b': 2,
                'column': 'c2'
            }
        ]
    }
    r = divide(KWARGS, CONTENTS)
    assert r['c1'][2] == 1
    assert r['c2'][2] == 2.0
