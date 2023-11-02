from typing import List, Set


def test_1():
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        for n in nums:
            if n - 1 not in nums_set:
                # нашли начало последовательности
                seq_len = 0
                while n + seq_len in nums_set:
                    seq_len += 1

                result = max(result, seq_len)

        return result
