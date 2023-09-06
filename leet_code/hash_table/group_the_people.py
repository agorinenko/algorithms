from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        meta = {}
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in meta:
                meta[size] = []

            meta[size].append(i)

        ans = []
        for size, peoples in meta.items():
            ans += [peoples[i:i + size] for i in range(0, len(peoples), size)]

        return ans

