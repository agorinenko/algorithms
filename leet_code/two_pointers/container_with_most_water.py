from typing import List


def test_1():
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

def test_2():
    assert Solution().maxArea([1, 1]) == 1


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1

        max_amount = 0
        while left_ptr < right_ptr:
            amount = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
            if amount > max_amount:
                max_amount = amount
            if height[left_ptr] <= height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_amount
