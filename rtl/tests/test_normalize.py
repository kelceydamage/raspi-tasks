from rtl.tasks.normalize import normalize
from dummy_data import KWARGS, CONTENTS3

def test_normalize():
    KWARGS = {
        'columns': [
            'a',
            'b'
        ],
        'model': 'DistanceFromMean',
        'weight': 0.01
    }
    r = normalize(KWARGS, CONTENTS3)
    assert r['bNormal'][2] == 10
    assert r['aNormal'][0] == 0