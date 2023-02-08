from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # [1] for fast linear-time detection of next-greater
        #    numbers we will maintain a decreasing stack
        stack = []

        # [2] provided that all numbers are unique, we can store
        #    their respective next-greater numbers in a map/dict
        nextg = dict()

        for n in nums2:
            # [3] once we encounter a number that is greater than some
            #    numbers from the top of the stack, it is obvious that
            #    this number is the next-greater for all of them
            while stack and stack[-1] < n:
                nextg[stack.pop()] = n
            stack.append(n)

        # [4] now, just process all queries
        return [nextg[n] if n in nextg else -1 for n in nums1]