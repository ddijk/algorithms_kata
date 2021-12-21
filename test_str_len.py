import pytest
from str_len import str_len

@pytest.mark.parametrize('input,expected', [
(['aap','noot','mies'], 11),
(['aap','noot','mies', 'vuur'], 15),
([], 0),
(['aap'], 3)
])
def test_str_len(input, expected):
    assert str_len(input) == expected
