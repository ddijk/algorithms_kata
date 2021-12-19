from intersection import intersect

import pytest

@pytest.mark.parametrize("expected,input_1,input_2",[
([2,4],[1, 2, 3, 4, 5],  [0, 2, 4, 6, 8]),
([2],[1, 2, 3, 7, 5],  [0, 2, 4, 6, 8])
])
def test_intersect(expected, input_1, input_2):
    assert expected == intersect(input_1,input_2)

