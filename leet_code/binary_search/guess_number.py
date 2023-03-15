# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pick = 1
    if num > pick:
        return -1
    if num < pick:
        return 1
    return 0


def test_guess_number():
    n = 1
    pick = 1
    assert pick == guess_number(n)


def guess_number(n: int) -> int:
    left = 0
    right = n
    while left <= right:
        middle = (left + right) // 2
        target = guess(middle)
        if target == 1:
            left = middle + 1
        elif target == -1:
            right = middle - 1
        else:
            return middle

    return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        return guess_number(n)
