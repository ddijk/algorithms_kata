import pytest
from double_array import double_array

@pytest.mark.parametrize('expected,input',[

    ([10],[5]),
    ([6, 8, 10],[3, 4, 5]),
    ([0, 2, 4, 6, 8, 10],[0, 1, 2, 3, 4, 5])

])
def test_double_array(expected, input):
    assert expected == double_array(input)
