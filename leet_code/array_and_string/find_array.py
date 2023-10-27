from typing import List


def test_1():
    assert Solution().findArray([5, 2, 0, 3, 1]) == [5, 7, 2, 3, 2]


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # arr =
        for i in range(1, len(pref)):
            pref[i] = pref[i - 1] ^ pref[i]

        return pref
