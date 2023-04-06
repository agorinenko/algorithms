from typing import List


def test_binary_search():
    arr = [4, 5, 6, 7, 0, 1, 2]
    assert 4 == Solution().search(arr, 0)


def test_binary_search_1():
    arr = [5, 1, 3]

    assert 0 == Solution().search(arr, 5)


def test_binary_search_2():
    arr = [4, 5, 6, 7, 0, 1, 2]
    assert -1 == Solution().search(arr, 3)


def find_min(nums: list[int]):
    if len(nums) == 1:
        return 0

    left, right = 0, len(nums) - 1

    if len(nums) == 2 and nums[left] < nums[right]:
        return left

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return left


def binary_search(arr: list[int], target: int) -> int:
    """
    Двоичный (бинарный) поиск (дихотомия)
    :param arr: массив для поиска.
    :param target: элемент, который нужно найти.
    :return: индекс элемента или -1 если не найдено
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        middle = arr[mid]
        if middle < target:
            left = mid + 1
        elif middle > target:
            right = mid - 1
        else:
            return mid
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sep = find_min(nums)

        first_array = nums[:sep]
        second_array = nums[sep:]
        res_1 = binary_search(first_array, target)
        res_2 = binary_search(second_array, target)
        if res_1 > -1:
            return res_1
        if res_2 > -1:
            return sep + res_2

        return -1
