from typing import List


def test_1():
    assert Solution().countDistinctIntegers([1, 13, 10, 12, 31]) == 6


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        extra = set(nums)
        cache = {}
        for i, n in enumerate(nums):
            if n in cache:
                new_n = cache[n]
            else:
                new_n = reverse_int(n) #637 ms 44.2 MB
                # n = reversed(str(n))  # 660 ms 44.1 MB
                # n = reverse_str(str(n))   # 926 ms 50.1 MB

                # new_n = int(''.join(n))
                cache[n] = new_n

            extra.add(new_n)

        return len(extra)


def reverse_int(x: int) -> int:
    rev = int(str(abs(x))[::-1])
    return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0


def reverse_str(s: str) -> str:
    arr = list(s)
    reverse_array(arr)
    return ''.join(arr)


def reverse_array(arr: List[str]) -> None:
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
