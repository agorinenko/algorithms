"""
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.
"""
from typing import List


def heappop(min_heap: list):
    min_heap.pop(0)


def heappush(min_heap: list, item: int):
    """
    1) Если в куче есть три числа, и если число больше наименьшего в минимальной куче,
    то удалите наименьшее число и вставьте число в кучу.
    2) Если в куче меньше трех элементов, просто добавьте число.
    """
    min_heap.append(item)
    min_heap.sort()


class Solution:
    def third_max(self, nums: List[int]) -> int:
        min_heap = []
        taken = set()

        for index in range(len(nums)):
            # If current number was already taken, skip it.
            if nums[index] in taken:
                continue

            # If min heap already has three numbers in it.
            # Pop the smallest if current number is bigger than it.
            if len(min_heap) == 3:
                if min_heap[0] < nums[index]:
                    taken.remove(min_heap[0])
                    heappop(min_heap)

                    heappush(min_heap, nums[index])
                    taken.add(nums[index])

            # If min heap does not have three number we can push it.
            else:
                heappush(min_heap, nums[index])
                taken.add(nums[index])

        # 'nums' has only one distinct element it will be the maximum.
        if len(min_heap) == 1:
            return min_heap[0]

        # 'nums' has two distinct elements.
        elif len(min_heap) == 2:
            first_num = min_heap[0]
            heappop(min_heap)
            return max(first_num, min_heap[0])

        return min_heap[0]

    def third_max_0(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        elem_counted = 1
        prev_elem = nums[0]

        for index in range(len(nums)):
            # Current element is different from previous.
            if nums[index] != prev_elem:
                elem_counted += 1
                prev_elem = nums[index]

            # If we have counted 3 numbers then return current number.
            if elem_counted == 3:
                return nums[index]

        # We never counted 3 distinct numbers, return largest number.
        return nums[0]
