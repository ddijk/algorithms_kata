from reverse import reverse
import pytest


@pytest.mark.parametrize('expected,input',[
('cba','abc'),
('aap','paa'),
('blah','halb')
])
def test_reverse(expected,input):
    assert expected == reverse(input)
