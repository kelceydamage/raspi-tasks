from rtl.tasks.null import null
from dummy_data import KWARGS, CONTENTS2

def null():
    r = task_null(KWARGS, CONTENTS2)
    assert r['a'][2] == 2
