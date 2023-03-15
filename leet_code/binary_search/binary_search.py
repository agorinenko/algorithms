from typing import List, Callable


def test_binary_search():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert 6 == binary_search(arr, 6)


def test_main_1():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert 0 == binary_search(nums, 1)
    assert 4 == binary_search(nums, 5)
    assert 5 == binary_search(nums, 6)
    assert 9 == binary_search(nums, 10)
    assert -1 == binary_search(nums, 11)


def test_main_2():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert 0 == binary_search(nums, 1)
    assert 4 == binary_search(nums, 5)
    assert 5 == binary_search(nums, 6)
    assert 9 == binary_search(nums, 10)
    assert -1 == binary_search(nums, 12)


def test_main_3():
    nums = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
    assert 0 == binary_search(nums, 1)
    assert 4 == binary_search(nums, 5)
    assert 5 == binary_search(nums, 6)
    assert 10 == binary_search(nums, 10)
    assert -1 == binary_search(nums, 12)


def test_binary_search_1():
    arr = []
    assert -1 == binary_search(arr, 6)


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
        return binary_search(nums, target)
