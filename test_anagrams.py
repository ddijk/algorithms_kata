from anagram import anagrams, add_one_per_word, add_one_to_result
import pytest


#@pytest.mark.skip
@pytest.mark.parametrize('expected,input',[
(['abc','acb','bca','bac','cab','cba'], 'abc'),
(['abc','acb','bca','bac','cab','cba'], 'acb'),
(['abc','acb','bca','bac','cab','cba'], 'bac')
])
def test_anagram(expected, input):
    assert sorted(expected) == sorted(anagrams(input))


def test_add_one_per_word():
    result = list(add_one_per_word('c', 'ab'))

    assert sorted(['abc','acb','cab']) == sorted(result)

def test_add_one_to_result():
    result = add_one_to_result('c', ['ab','ba'])

    assert sorted(['abc','acb','cab', 'bac','bca','cba']) == sorted(result)

