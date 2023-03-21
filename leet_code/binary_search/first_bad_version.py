# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version > 17


def test_main_1():
    assert 6 == Solution().firstBadVersion(10)

def test_main_2():
    assert 18 == Solution().firstBadVersion(20)


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
