from typing import List


def test_1():
    a = 100000
    b = 100000
    assert id(a) == id(b)  # true or false?

    # assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, n in enumerate(nums):
            if n in num_dict:
                num_dict[n].append(i)
            else:
                num_dict[n] = [i]

        for i, n in enumerate(nums):
            delta = target - n
            if delta in num_dict and delta != n:
                return [i, num_dict[delta][0]]

            if delta in num_dict and delta == n and len(num_dict[delta]) > 1:
                return num_dict[delta]

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
