def test_1():
    assert Solution().climbStairs(2) == 2


class Solution:
    def climbStairs(self, n: int) -> int:
        memory = [None] * (n + 1)
        memory[0] = 1
        memory[1] = 1

        def climb(n):
            if memory[n]:
                return memory[n]

            if n == 0:
                return 1
            if n == 1:
                return 1

            res = climb(n - 1) + climb(n - 2)
            memory[n] = res
            return res

        return climb(n)


"""
int fac_times (int n, int acc) {
    return (n==0) ? acc : fac_times(n - 1, acc * n);
}
int factorial (int n) {
    return fac_times (n, 1);
}
"""


def factorial2(n: int, acc: int) -> int:
    if n == 0:
        return acc

    return factorial2(n - 1, acc * n)


def factorial(n: int) -> int:
    if n == 0:
        return 1

    return n * factorial(n - 1)
