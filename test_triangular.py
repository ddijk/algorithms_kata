import pytest

from triangular import triangular

@pytest.mark.parametrize('input, expected',[

    (7, 28),
    (3, 6)
])
def test_triag(input, expected):
    assert triangular(input) == expected
