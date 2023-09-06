from typing import List


def count_set_bits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count


def test_count_set_bits():
    assert 2 == count_set_bits(5)


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for _ in range(n + 1)]
        for i in range(n + 1):
            ans[i] = count_set_bits(i)
        return ans
