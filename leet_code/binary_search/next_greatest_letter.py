from typing import List


def left_binary_search(left: int, right: int, check, *args):
    """
    Левый бинарный поиск. Задача нахождения первого подходящего значения
    ___плохо___|---хорошо---
    :param left: указатель на минимальное значение функции
    :param right: указатель на максимальное значение функции
    :param check: функция проверки условия
    :param args: аргументы функции проверки условия
    :return: индекс первого элемента, удовлетворяющего условию
    """
    while left < right:
        mid = (left + right) // 2
        if check(mid, *args):
            right = mid
        else:
            left = mid + 1

    return left


def next_greatest_letter(letters: List[str], target: str):
    left = 0
    right = len(letters) - 1

    def find_target(mid):
        return letters[mid] > target

    idx = left_binary_search(left, right, find_target)
    c = letters[idx]
    if c > target:
        return c

    return letters[0]


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return next_greatest_letter(letters, target)
