from typing import List, Optional


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reverse_string_recursion(s)


def test_1():
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    assert s == ["o", "l", "l", "e", "h"]


def test_2():
    s = ["H", "a", "n", "n", "a", "h"]
    reverse_string(s)
    assert s == ["h", "a", "n", "n", "a", "H"]


def test_3():
    s = ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ", "a", " ", "c", "a", "n", "a", "l",
         ":", " ", "P", "a", "n", "a", "m", "a"]

    expected = ["a", "m", "a", "n", "a", "P", " ", ":", "l", "a", "n", "a", "c", " ", "a", " ", ",", "n", "a", "l",
                "p", " ", "a", " ", ",", "n", "a", "m", " ", "A"]

    reverse_string(s)
    assert s == expected


def reverse_string(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_string_recursion(s: List[str], left: Optional[int] = 0) -> None:
    right = -(left + 1)
    if left > (len(s) // 2) - 1:
        return None

    reverse_string_recursion(s, left + 1)
    s[left], s[right] = s[right], s[left]
