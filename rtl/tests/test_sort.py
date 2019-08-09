from rtl.tasks.sort import sort
from dummy_data import KWARGS, CONTENTS2

def test_sort():
    KWARGS= {
        'axis': 0,
        'method': 'quicksort',
        'column': 'b'
    }
    r = sort(KWARGS, CONTENTS2)
    assert r['a'][2] == 1
