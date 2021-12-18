from merge_sort import merge_sort, merge
import pytest

@pytest.mark.skip(reason="no way of currently testing this")
def test_already_sorted():
    assert [1,2,3,4,5,6,7,8]==merge_sort([1,2,3,4,5,6,7,8])

def test_sort_1():
    assert [1,2,3,4,5,6,7,8]==merge_sort([1,2,3,5,4,6,7,8])

def test_sort_2():
    assert [1,2,3,4,5,6,7,8]==merge_sort([8,2,3,5,7,6,4,1])

def test_merge_1():
    assert [1,2,3] == merge([], [1,2,3])

def test_merge_2():
    assert [1,2,3] == merge([1,2,3], [])

def test_merge_3():
    assert [1,2,3] == merge([1,3], [2])

def test_merge_4():
    assert [1,2,3] == merge([2], [1,3])

def test_merge_5():
    assert [1,2,3,4] == merge([2,4], [1,3])

def test_merge_6():
    assert [1,2,3,4] == merge([1,3], [2,4])

def test_merge_7():
    assert [1,2,3,4,5,6,7,8] == merge([1,3,5,6], [2,4,7,8])

def test_merge_8():
    assert [1,2,3,4,5,6,7,8] == merge([2,4,7,8], [1,3,5,6])

def test_merge_9():
    assert [1,2,2, 3, 3,4,5,6,7,8] == merge([2,4,7,8], [1,2,3,3,5,6])

def test_merge_10():
    assert [1,2,2, 3, 3,4,5,6,7,8] == merge([1,2,3,3,5,6],[2,4,7,8])
