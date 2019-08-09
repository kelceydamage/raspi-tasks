import rtl.tasks.squareRoot as s
print(dir(s))

from rtl.tasks.squareRoot import squareRoot
from dummy_data import KWARGS, CONTENTS3

def test_squareRoot():
    KWARGS = {
        'operations': [
            {
                'a': 'b',
                'column': 'c'
            }
        ]
    }
    r = squareRoot(KWARGS, CONTENTS3)
    assert r['c'][2] == 3.605551275463989
