from math_series.series import fibonacci_one, lucas, sum_series
import pytest
# actual = function return
# expected = expecting it to return
# assert actual is == to expected

# @pytest.mark.skip(reason="no yet")
def test_fibonacci_one_a():
    n = 1
    actual = fibonacci_one(1)
    expected = n
    assert actual == expected

# @pytest.mark.skip(reason="no yet")
def test_fibonacci_one_b():
    actual = fibonacci_one(0)
    expected = 0
    assert actual == expected

# @pytest.mark.skip(reason="no yet")
def test_fibonacci_one_c():
    actual = fibonacci_one(9)
    expected = 34
    assert actual == expected

# @pytest.mark.skip(reason="no yet")
def test_lucas_a():
    actual = lucas(1)
    expected = 1
    assert actual == expected

# @pytest.mark.skip(reason="no yet")
def test_lucas_b():
    actual = lucas(0)
    expected = 2
    assert actual == expected


# @pytest.mark.skip(reason="no yet")
def test_lucas_c():
    actual = lucas(5)
    expected = 11
    assert actual == expected

# @pytest.mark.skip(reason="no yet")
def test_sum_series_a():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

# @pytest.mark.skip(reason="no yet")
def test_sum_series_b():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

# @pytest.mark.skip(reason="no yet")
def test_sum_series_c():
    actual = sum_series(5, 5)
    expected = 20
    assert actual == expected
