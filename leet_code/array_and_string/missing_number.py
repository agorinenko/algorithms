from typing import List


def test_1():
    assert Solution().missingNumber([3, 0, 1]) == 2
    # 0+1+2+3=6
    # 4*4/2=


def test_2():
    # 0+1+2=3
    # 2 * (2+1)/2
    assert Solution().missingNumber([0, 1]) == 2


def test_3():
    # 0+1+2+3+4+5+6+7+8+9=45
    # sum = len * (len+1)/2
    # 9 *(9+1)/2
    assert Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        origin = range(0, len(nums) + 1)

        return sum(origin) - sum(nums)

    def missingNumber3(self, nums: List[int]) -> int:
        sum_origin = int(len(nums) * (len(nums) + 1) / 2)

        return sum_origin - sum(nums)

    def missingNumber2(self, nums: List[int]) -> int:
        i = max(nums)
        if i == len(nums):
            origin = range(0, i + 1)
        else:
            origin = range(0, i + 2)

        return sum(origin) - sum(nums)
