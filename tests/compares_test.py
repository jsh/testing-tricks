import pytest

from compares import (
    are_equal,
    are_not_equal,
    is_greater,
    is_less,
    is_greater_or_equal,
    is_less_or_equal,
)


# Define test cases once
TEST_CASES = [
    (5, 3),  # a > b
    (3, 3),  # a == b
    (2, 3),  # a < b
    (-1, -2),  # negative numbers, a > b
    (-2, -2),  # negative numbers, a == b
    (-3, -2),  # negative numbers, a < b
    (0, 0),  # zeros
    (0, 1),  # zero less than positive
    (1, 0),  # positive greater than zero
    (1.5, 1.2),  # floats, a > b
    (1.2, 1.2),  # floats, a == b
    (1.1, 1.2),  # floats, a < b
]

EQ_TEST_CASES = [
    (a, b, True if a == b else False)
    for a, b in TEST_CASES  # type ignore
]

NE_TEST_CASES = [
    (a, b, True if a != b else False)
    for a, b in TEST_CASES  # type ignore
]

GT_TEST_CASES = [
    (a, b, True if a > b else False)
    for a, b in TEST_CASES  # type ignore
]

LT_TEST_CASES = [
    (a, b, True if a < b else False)
    for a, b in TEST_CASES  # type ignore
]

GE_TEST_CASES = [
    (a, b, True if a >= b else False)
    for a, b in TEST_CASES  # type ignore
]

LE_TEST_CASES = [
    (a, b, True if a <= b else False)
    for a, b in TEST_CASES  # type ignore
]


@pytest.mark.parametrize("a, b, expected", EQ_TEST_CASES)
def test_are_equal(a, b, expected):
    assert are_equal(a, b) is expected


@pytest.mark.parametrize("a, b, expected", NE_TEST_CASES)
def test_are_not_equal(a, b, expected):
    assert are_not_equal(a, b) is expected


@pytest.mark.parametrize("a, b, expected", GT_TEST_CASES)
def test_is_greater(a, b, expected):
    assert is_greater(a, b) is expected


@pytest.mark.parametrize("a, b, expected", LT_TEST_CASES)
def test_is_less(a, b, expected):
    assert is_less(a, b) is expected


@pytest.mark.parametrize("a, b, expected", GE_TEST_CASES)
def test_is_greater_or_equal(a, b, expected):
    assert is_greater_or_equal(a, b) is expected


@pytest.mark.parametrize("a, b, expected", LE_TEST_CASES)
def test_is_less_or_equal(a, b, expected):
    assert is_less_or_equal(a, b) is expected
