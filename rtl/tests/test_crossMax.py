from rtl.tasks.crossMax import crossMax
from dummy_data import KWARGS, CONTENTS

def test_crossMax():
    KWARGS = {
        'operations': [
            {
                'columns': ['a', 'b'],
                'column': 'c1'
            }
        ]
    }
    r = crossMax(KWARGS, CONTENTS)
    assert r['c1'][2] == 4.0
