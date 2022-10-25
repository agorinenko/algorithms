"""
https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/
"""


class Solution:
    def is_happy_1(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

    def is_happy(self, n: int) -> bool:

        def _parts(n: int) -> list[int]:
            res = []
            while n > 0:
                res.append(n % 10)
                n = n // 10

            res.reverse()
            return res

        def _sum(res: list[int]) -> int:
            s = 0
            for i in res:
                s += i ** 2
            return s

        while True:
            parts = _parts(n)
            n = _sum(parts)
            if n == 1 or n == 7:
                return True

            if n < 10:
                return False
