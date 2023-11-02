from typing import List


def test_1():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, n in enumerate(nums):
            delta = target - n

            if delta in num_dict:
                return [num_dict[delta], i]
            else:
                num_dict[n] = i

        return []

    def two_sum2(self, numbers: List[int], target: int) -> List[int]:
        num_set = set(numbers)
        for idx in range(len(numbers)):
            f = numbers[idx]
            s = target - f
            if s in num_set:
                for idx2 in range(idx + 1, len(numbers)):
                    if s == numbers[idx2]:
                        return [idx + 1, idx2 + 1]

        return []

    def two_sum_slow(self, numbers: List[int], target: int) -> List[int]:
        for idx in range(len(numbers)):
            for idx2 in range(idx + 1, len(numbers)):
                if numbers[idx] + numbers[idx2] == target:
                    return [idx + 1, idx2 + 1]

        return []
