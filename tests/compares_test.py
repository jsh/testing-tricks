import pytest

from compares import is_greater_or_equal, is_less_or_equal


# Define test cases once
GE_TEST_CASES = [
    (5, 3, True),  # a > b
    (3, 3, True),  # a == b
    (2, 3, False),  # a < b
    (-1, -2, True),  # negative numbers, a > b
    (-2, -2, True),  # negative numbers, a == b
    (-3, -2, False),  # negative numbers, a < b
    (0, 0, True),  # zeros
    (0, 1, False),  # zero less than positive
    (1, 0, True),  # positive greater than zero
    (1.5, 1.2, True),  # floats, a > b
    (1.2, 1.2, True),  # floats, a == b
    (1.1, 1.2, False),  # floats, a < b
]


# Test cases for less_or_equal are the same but with inverted expectations
# except for equality cases which remain True
LE_TEST_CASES = [
    (a, b, not expected if a != b else True)
    for a, b, expected in GE_TEST_CASES  # type: ignore
]


@pytest.mark.parametrize("a, b, expected", GE_TEST_CASES)
def test_is_greater_or_equal(a, b, expected):
    assert is_greater_or_equal(a, b) is expected


@pytest.mark.parametrize("a, b, expected", LE_TEST_CASES)
def test_is_less_or_equal(a, b, expected):
    assert is_less_or_equal(a, b) is expected
