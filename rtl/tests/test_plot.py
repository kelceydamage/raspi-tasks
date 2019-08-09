from rtl.tasks.simplePlot import simplePlot
from rtl.tasks.simplePlot import PLOT_QUEUE
from dummy_data import KWARGS, CONTENTS

def test_simplePlot():
    KWARGS = {
        'plots': {
            'test': [
                {
                    'x': 'a',
                    'y': 'b',
                    'type': 'circle',
                    'scale': 'linear',
                    'series': None
                },
                {
                    'x': 'a',
                    'y': 'b',
                    'type': 'circle',
                    'scale': 'linear',
                    'series': 'a'
                }
            ]
        }
    }
    r = simplePlot(KWARGS, CONTENTS)
    q = PLOT_QUEUE.get()
    assert q['draws'][0]['x'][0] == 4
    assert q['draws'][1]['x'][0] == 4
