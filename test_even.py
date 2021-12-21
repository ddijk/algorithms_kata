import pytest
from even import even_only

@pytest.mark.parametrize('input,expected',[
  ([1,3,4,5,6], [4,6]),
  ([1,2, 3,4,5,6], [2, 4,6]),
  ([], [])
])
def test_even(input,expected):
    assert sorted(even_only(input)) == sorted(expected)
