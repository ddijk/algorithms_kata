import pytest
from string_x import first
import string

@pytest.mark.parametrize('input,expected', [
  (string.ascii_lowercase, 23),
  ('ax', 1), 
  ('', -1),
  ('x', 0) 
])
def test_first(input,expected):
    assert first(input) == expected
