from typing import List

def test_1():
    assert 7 == Solution().minExtraChar("dwmodizxvvbosxxw", ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"])

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = sorted(dictionary, key=lambda x: len(x), reverse=True)
        for w in dictionary:
            a = s.split(w)
            s = ''.join(a)

        return len(s)
