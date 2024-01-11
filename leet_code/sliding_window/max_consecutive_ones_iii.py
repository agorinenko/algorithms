from typing import List


def test_1():
    assert Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6


def test_2():
    assert Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10


def test_3():
    assert Solution().longestOnes([0, 0, 0, 1], 4) == 4


def test_4():
    assert Solution().longestOnes([1, 0, 0, 0, 1, 1], 1) == 3


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, res = 0, 0, 0

        while right < len(nums):
            cur_num = nums[right]
            if cur_num == 0:
                k -= 1

            if k < 0:
                left_num = nums[left]
                if left_num == 0:
                    k += 1
                left += 1

            right += 1

        return right - left
