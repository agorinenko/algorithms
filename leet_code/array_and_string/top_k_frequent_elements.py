import collections
from typing import List


def test_1():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert Solution().topKFrequent(nums, k) == [1, 2]


def test_2():
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    assert Solution().topKFrequent(nums, k) == [-1, 2]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = collections.defaultdict(int)
        for n in nums:
            hash_map[n] += 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, pos in hash_map.items():
            freq[pos].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            row = freq[i]
            for num in row:
                res.append(num)
                if len(res) == k:
                    return res

        return []

        # O(n*log(n))
        # sorted_keys = [k for k, _ in sorted(hash_map.items(), key=lambda x: x[1], reverse=True)]
        # keys = sorted_keys[:k]
        # return keys
