"""
https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/
"""


class Solution:
    def numSquares(self, n: int) -> int:
        level = 0
        targets = {n}
        roots = {(x + 1) ** 2 for x in range(int(n ** 0.5))}

        while targets:
            i = targets & roots
            if i:
                targets = None
            else:
                targets = {x - y for x in targets for y in roots if x - y > 0}

            level += 1

        return level
