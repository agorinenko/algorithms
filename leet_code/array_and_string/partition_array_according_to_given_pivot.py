from typing import List


def test_1():
    assert Solution().pivotArray([9, 12, 5, 10, 14, 3, 10], 10) == [9, 5, 3, 10, 10, 12, 14]


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        center_arr = []
        left_arr = []
        right_arr = []

        for num in nums:
            if num == pivot:
                center_arr.append(num)
            elif num < pivot:
                left_arr.append(num)
            else:
                right_arr.append(num)

        return left_arr + center_arr + right_arr
