from merge_sort import merge_sort, merge
import pytest


@pytest.mark.parametrize(
    "expected,input", [([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8])]
)
def test_already_sorted(expected, input):
    assert expected == merge_sort(input)


@pytest.mark.parametrize(
    "expected,input",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 5, 4, 7, 6, 8]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [8, 2, 3, 5, 7, 6, 4, 1]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 5, 4, 6, 7, 8]),
    ],
)
def test_merge_sort(expected, input):
    assert expected == merge_sort(input)


@pytest.mark.parametrize(
    "expected,left,right",
    [
        ([1, 2, 3], [], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3], []),
        ([1, 2, 3], [1, 3], [2]),
        ([1, 2, 3], [2], [1, 3]),
        ([1, 2, 3, 4], [2, 4], [1, 3]),
        ([1, 2, 3, 4], [1, 3], [2, 4]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 5, 6], [2, 4, 7, 8]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [2, 4, 7, 8], [1, 3, 5, 6]),
        ([1, 2, 2, 3, 3, 4, 5, 6, 7, 8], [2, 4, 7, 8], [1, 2, 3, 3, 5, 6]),
        ([1, 2, 2, 3, 3, 4, 5, 6, 7, 8], [1, 2, 3, 3, 5, 6], [2, 4, 7, 8]),
    ],
)
def test_merge(expected, left, right):
    assert expected == merge(left, right)
