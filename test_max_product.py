from max_product import max_prod
import pytest

@pytest.mark.parametrize('expected,input',[
(4, [2,2]),
(4, [-2, -2, 1, 3]),
(54, [5, -10, 6, 9, 4]),
(60, [5, -10, -6, 9, 4])
])
def test_max_prod(expected, input):
    assert expected == max_prod(input)
