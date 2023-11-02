import collections
from typing import List, Union


def test_1():
    assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["bat"], ["nat", "tan"],
                                                                                    ["ate", "eat", "tea"]]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = collections.defaultdict(list)
        for s in strs:
            key = _encode_anagram2(s)
            map[key].append(s)
        return list(map.values())


def _encode_anagram2(s: str) -> Union[str, tuple]:
    """
    ddddgge -> [0]*26
    """
    count = [0] * 26
    a_idx = ord('a')
    for c in s:
        count[ord(c) - a_idx] += 1

    return tuple(count)


def _encode_anagram(s: str) -> Union[str, tuple]:
    """
    ddddgge ->d4g2e
    """
    map = collections.defaultdict(int)
    for c in s:
        map[c] += 1

    arr = []
    sorted_keys = sorted(map.keys())
    for k in sorted_keys:
        arr.append(k)
        arr.append(str(map[k]))

    return ''.join(arr)
