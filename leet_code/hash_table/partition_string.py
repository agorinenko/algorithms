def test_1():
    assert Solution().partitionString("abacaba") == 4


def test_2():
    assert Solution().partitionString("ssssss") == 6


class Solution:
    def partitionString(self, s: str) -> int:
        i = 1
        sub = set()
        ans = []
        for c in s:
            if c not in sub:
                sub.add(c)
            else:
                i += 1
                ans.append(sub)
                sub = {c}

        return i
