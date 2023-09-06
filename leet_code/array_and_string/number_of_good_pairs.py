from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1

        ans = 0
        for n in m.values():
            ans += n * (n - 1) // 2

        return ans
