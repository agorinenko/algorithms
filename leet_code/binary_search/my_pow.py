def test_maim_1():
    assert 0.25000 == Solution().myPow(2, -2)


def test_maim_2():
    assert 1024.00000 == Solution().myPow(2, 10)


def pow(x: float, n: int) -> float:
    is_negative = n < 0
    n = abs(n)
    res = 1 / recursive_pow(x, n) if is_negative else recursive_pow(x, n)
    return res


def recursive_pow(x: float, n: int) -> float:
    if n == 0:
        return 1

    if n == 1:
        return x

    res = recursive_pow(x, int(n / 2))

    if n % 2 == 0:
        return res * res

    return res * res * x


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)
