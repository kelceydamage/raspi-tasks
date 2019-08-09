from rtl.tasks.classifyStatic import classifyStatic
from dummy_data import KWARGS, CONTENTS3

def test_classifyStatic():
    KWARGS = {
        'operations': [
            {
                'a': ['a', 'b'],
                'column': 'c1'
            },
        ]
    }
    r = classifyStatic(KWARGS, CONTENTS3)
    assert r['c1Class'][2] == 3
    assert r['c1ClassCount'][2] == 1
    KWARGS = {
        'operations': [
            {
                'a': 'a',
                'column': 'c1'
            },
        ]
    }
    r = classifyStatic(KWARGS, CONTENTS3)
    assert r['c1Class'][2] == 2
    assert r['c1ClassCount'][2] == 1
