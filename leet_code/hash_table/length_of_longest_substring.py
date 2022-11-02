"""
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1135/
"""


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

    def length_of_longest_substring2(self, s: str) -> int:
        if len(s) == 1:
            return 1
        res_data = set()
        for idx in range(len(s)):
            data = set(s[idx])
            for idx2 in range(idx + 1, len(s)):
                if s[idx2] not in data:
                    data.add(s[idx2])
                else:
                    if len(data) > len(res_data):
                        res_data = data
                    break

            if len(data) > len(res_data):
                res_data = data

        return len(res_data)
