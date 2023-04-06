from typing import List


def test_main_1():
    nums = [1, 2, 1, 3, 5, 6, 4]
    assert Solution().findPeakElement(nums) in [1, 5]


def test_main_2():
    nums = [1, 2, 3, 1]
    assert Solution().findPeakElement(nums) in [2]


def test_main_3():
    nums = [1, 2]
    assert Solution().findPeakElement(nums) == 1


def test_main_4():
    nums = [1, 2, 3]
    assert Solution().findPeakElement(nums) == 2


def test_main_5():
    nums = [1, 2, 3, 1]
    assert Solution().findPeakElement(nums) == 2


def test_main_6():
    nums = [1, 3, 2, 1]
    assert Solution().findPeakElement(nums) == 1


def find_max_element(nums: list[int]) -> int:
    """
    Нахождение локального максимума
    :param nums: последовательность чисел
    :return: индекс максимума
    """
    if len(nums) == 1:
        return 0

    left, right = 0, len(nums) - 1

    if len(nums) == 2 and nums[left] < nums[right]:
        return right

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return find_max_element(nums)
