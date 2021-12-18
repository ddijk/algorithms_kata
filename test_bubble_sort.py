
from bubble_sort import bubble_sort

def test_sort_already_sorted():
    assert [1,2,3,4,5,6,7,8]==bubble_sort([1,2,3,4,5,6,7,8])

def test_sort_1():
    assert [1,2,3,4,5,6,7,8]==bubble_sort([1,2,8,7,5,6,4,3])

def test_sort_2():
    assert [1,2,3,4,5,6,7,8]==bubble_sort([8,2,1,7,5,6,3,4])


