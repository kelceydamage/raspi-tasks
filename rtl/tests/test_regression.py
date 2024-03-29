from rtl.tasks.regression import regression
from dummy_data import KWARGS, CONTENTS3

def test_linearRegression():
    KWARGS = {
        'operations': [
            {
                'x': 'a',
                'y': 'b',
                'space': 'linear',
                'model': 'Linear'
            },
        ]
    }
    r = regression(KWARGS, CONTENTS3)
    assert r['bLinear'].tolist() == [
        10.500000000000002, 11.000000000000002, 11.5, 12.0
    ]

def test_polyRegression():
    KWARGS = {
        'operations': [
            {
                'x': 'a',
                'y': 'b',
                'space': 'linear',
                'model': 'Poly',
                'd': 3
            },
        ]
    }
    r = regression(KWARGS, CONTENTS3)
    assert r['bPoly'].tolist() == [
        2.000000000000078, 23.000000000000068, 13.000000000000064, 7.000000000000071
    ]
    #[2.000000000000078, 23.000000000000046, 13.000000000000021, 6.999999999999964]
    # Precision is system dependant and often this test will fail.
