import math
from typing import List


class Solution:
    def find_restaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_list = list1 if len(list1) < len(list2) else list2
        max_list = list1 if len(list1) >= len(list2) else list2

        map_idx = {}
        for idx in range(len(min_list)):
            map_idx[min_list[idx]] = idx

        min_sum = math.inf
        res = []
        for idx, word in enumerate(max_list):
            if word in map_idx:
                cur_sum = idx + map_idx[word]

                if cur_sum < min_sum:
                    min_sum = cur_sum
                    res = [word]
                elif cur_sum == min_sum:
                    res.append(word)

        return res
