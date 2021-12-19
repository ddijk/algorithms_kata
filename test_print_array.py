from print_array import print_numbers
import pytest


@pytest.mark.parametrize(
    "expected,input", [
        ([55], [55]), 
        ([2, 4], [2, 4]), 
        ([2, 4, 1, 3], [2, 4, [1, 3]])],
)
def test_print(expected, input):
    assert expected == print_numbers(input)
