from typing import List, Optional


def test_1():
    nums = [-1, 0, 1, 2, -1, -4]
    assert Solution().threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]


def test_2():
    nums = [0, 0, 0]
    assert Solution().threeSum(nums) == [[0, 0, 0]]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            left_ptr = i + 1
            right_ptr = len(nums) - 1
            while left_ptr < right_ptr:
                s = num + nums[left_ptr] + nums[right_ptr]
                if s < 0:
                    left_ptr += 1
                elif s > 0:
                    right_ptr -= 1
                else:
                    result.append([num, nums[left_ptr], nums[right_ptr]])
                    left_ptr += 1
                    while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr - 1]:
                        left_ptr += 1

        return result
