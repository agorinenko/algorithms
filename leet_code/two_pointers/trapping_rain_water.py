from typing import List


def test_1():
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


class Solution:
    def trap(self, height: List[int]) -> int:
        left_ptr, right_ptr = 0, len(height) - 1
        total = 0
        left_max = height[left_ptr]
        right_max = height[right_ptr]
        while left_ptr < right_ptr:
            if left_max < right_max:
                left_ptr += 1
                left_max = max(left_max, height[left_ptr])
                total += left_max - height[left_ptr]
            else:
                right_ptr -= 1
                right_max = max(right_max, height[right_ptr])
                total += right_max - height[right_ptr]

        return total
