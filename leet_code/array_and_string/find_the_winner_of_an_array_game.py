import collections
from typing import List


def test_1():
    assert Solution().getWinner([2, 1, 3, 5, 4, 6, 7], 2) == 5


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        
        d = collections.deque(arr)
        wins_count = 0
        prew_winner = None

        while wins_count != k:
            first = d.popleft()
            second = d.popleft()

            winner = max(first, second)
            if winner == first:
                d.append(second)
                d.appendleft(first)
            else:
                d.append(first)
                d.appendleft(second)

            if prew_winner == winner:
                wins_count += 1
            else:
                prew_winner = winner
                wins_count = 1

        return prew_winner
