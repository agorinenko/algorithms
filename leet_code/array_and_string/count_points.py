import math
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for circle in queries:
            c = 0
            for point in points:
                dist = math.dist(point, [circle[0], circle[1]])
                if dist <= circle[2]:
                    c += 1

            ans.append(c)
        return ans
