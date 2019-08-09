from rtl.tasks.columnSpace import columnSpace
from dummy_data import KWARGS, CONTENTS3

def test_columnSpace():
    KWARGS = {
        'column': 'b',
        'space': 'linear',
    }
    r = columnSpace(KWARGS, CONTENTS3)
    assert r['bSpace'][2] == 15
