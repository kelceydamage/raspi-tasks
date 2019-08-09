from rtl.tasks.unique import unique
from dummy_data import KWARGS, CONTENTS

def test_unique():
    KWARGS = {
        'a': 'a',
        'column': 'c1'
    }
    r = unique(KWARGS, CONTENTS)
    assert r['a'][0] == 4
    assert r['b'][0] == 4
