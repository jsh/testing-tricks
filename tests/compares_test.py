import pytest

from compares import is_greater_or_equal


@pytest.mark.parametrize(
    "a, b, expected",
    [
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
    ],
)
def test_is_greater_or_equal(a, b, expected):
    assert is_greater_or_equal(a, b) == expected
