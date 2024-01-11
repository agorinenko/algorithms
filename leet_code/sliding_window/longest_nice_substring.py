

def test_1():
    assert Solution().longestNiceSubstring("YazaAay") == "aAa"


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ''

        seen = set(s)

        for i, cur_char in enumerate(s):
            if cur_char.lower() in seen and cur_char.upper() in seen:
                continue

            left = self.longestNiceSubstring(s[:i])
            right = self.longestNiceSubstring(s[i + 1:])

            return max(left, right, key=len)

        return s

    def longestNiceSubstring2(self, s: str) -> str:
        left = 0
        res = ''
        while left < len(s):
            for right in range(left + 1, len(s) + 1):
                sub_str = s[left:right]
                if is_nice(sub_str) and len(sub_str) > len(res):
                    res = sub_str

            left += 1

        return res


def is_nice(s: str) -> bool:
    if len(s) < 2:
        return False

    memory = set(s)
    for c in s:
        b = c.lower() in memory and c.upper() in memory
        if not b:
            return False

    return True