import collections


def test_1():
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1) Определяем левую и правую границу. Размер окна может быть фиксированного размера или динамическим
        # (зависит от какого-то условия)
        memory, left, res = collections.defaultdict(int), 0, 0
        for right, cur_char in enumerate(s):
            pass

        return res


def success(s: str, t: str) -> bool:
    """
    Символы строки s покрывают ВСЕ символы t
    s="BANC", t = "ABC" -> True
    """
    uniq = set(t)
    for c in s:
        if c in uniq:
            uniq.remove(c)

        if not uniq:
            return True

    return False
