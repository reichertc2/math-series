from math_series.series import fibonacci_one

# actual = function return
# expected = expecting it to return
# assert actual is == to expected


def test_fibonacci_one_a():
    n = 0
    actual = fibonacci_one(2)
    expected = [n, n, n, n]
    assert actual == expected

def test_fibonacci_one_b():
    n = 0
    actual = fibonacci_one(4)
    expected = [n, n, n, n,n,n]
    assert actual == expected
