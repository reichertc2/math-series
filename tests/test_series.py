from math_series.series import fibonacci_one
import pytest
# actual = function return
# expected = expecting it to return
# assert actual is == to expected


def test_fibonacci_one_a():
    n = 1
    actual = fibonacci_one(1)
    expected = n
    assert actual == expected


def test_fibonacci_one_b():
    n = 0
    actual = fibonacci_one(2)
    expected = [n, 1, 1]
    assert actual == expected


@pytest.mark.skip(reason="no yet")
def test_fibonacci_one_c():
    n = 0
    actual = fibonacci_one(9)
    expected = 34
    assert actual == expected
