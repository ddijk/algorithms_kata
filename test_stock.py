import pytest

from stock import max_profit

@pytest.mark.parametrize('expected,input',[
(4,[1,2,4,5]),
(6, [10, 7, 5, 8, 11, 2, 6]),
(7, [10, 7, 5, 8, 11, 2, 9]),
(0, [2,2,2]),
(7, [10, 7, 5, 8, 11, 2, 9, 3])
])
def test_profit(expected, input):
    assert expected == max_profit(input)
