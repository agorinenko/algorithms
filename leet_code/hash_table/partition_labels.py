from typing import List


def test_1():
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]


def test_2():
    assert Solution().partitionLabels("eccbbbbdec") == [10]


def test_3():
    assert Solution().partitionLabels("qiejxqfnqceocmy") == [13, 1, 1]


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        ans = []
        part = []
        letters = {s[0]}
        last_idx = last[s[0]]
        for i, c in enumerate(s):
            if i <= last_idx:
                part.append(c)
                letters.add(c)

                last_idx_candidate = last[c]
                if last_idx < last_idx_candidate:
                    last_idx = last_idx_candidate
            else:
                ans.append(''.join(part))
                part = [c]
                letters = {c}
                last_idx = last[c]

        ans.append(''.join(part))

        return [len(x) for x in ans]
