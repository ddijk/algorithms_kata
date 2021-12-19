from merge_sort import merge_sort
from bubble_sort import bubble_sort
import pytest


@pytest.mark.parametrize(
    "expected,input",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 8, 7, 5, 6, 4, 3]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [8, 2, 1, 7, 5, 6, 3, 4]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]), # already sorted
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 5, 4, 7, 6, 8]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [8, 2, 3, 5, 7, 6, 4, 1]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 5, 4, 6, 7, 8]),
    ],
)
class TestSort:
    def test_merge_sort(self, expected, input):
        assert expected == merge_sort(input)

    def test_bubble_sort(self, expected, input):
        assert expected == bubble_sort(input)
