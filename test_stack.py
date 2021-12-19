from stack import Stack


def test_stack():
    s = Stack()

    s.push('a')
    s.push('b')

    assert 'b'==s.pop()
    assert 'a'==s.pop()


def test_empty_stack():
    s = Stack()

    assert not s.pop()
