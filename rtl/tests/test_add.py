from rtl.tasks.add import add
from dummy_data import KWARGS, CONTENTS

def test_add():
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
    r = add(KWARGS, CONTENTS)
    assert r['c1'][2] == 8
    assert r['c2'][2] == 5.0
