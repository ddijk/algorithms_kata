import pytest
from reverse_string import reverse


@pytest.mark.parametrize('expected,input',[

  ('edcba', 'abcde'),
  ('a','a'),
  ('ab','ba')
])
def test_reverse(expected, input):
    assert expected == reverse(input)
