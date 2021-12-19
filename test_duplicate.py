from duplicate import find_duplicate, find_first_non_duplicated_char, find_missing_letter

import pytest


@pytest.mark.parametrize(
    "expected,input",
    [
        ("c", ["a", "b", "c", "d", "c", "e", "f"]),
        ("f", ["a", "b", "f", "d", "c", "e", "f"]),
        (None, ["a", "b", "f", "d", "c", "e", "g"]),
    ],
)
def test_find_duplicate(expected, input):
    assert expected == find_duplicate(input)


@pytest.mark.parametrize(
    "expected,input", [("f", "the quick brown box jumps over a lazy dog")]
)
def test_find_missing_letter(expected, input):
    assert expected == find_missing_letter(input)


@pytest.mark.parametrize('expected,input',[
    ('n', 'minimum'),
    ('a', 'maximum'),
    (None, 'aabbcc')
])
def test_find_first_non_duplicate_letter(expected, input):
    assert expected == find_first_non_duplicated_char(input)

