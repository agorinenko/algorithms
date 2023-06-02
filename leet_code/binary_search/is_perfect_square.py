def is_perfect_square(target: int) -> int:
    if target == 1:
        return 1
    left = 0
    right = target - 1

    def find_target(mid):
        return mid * mid <= target

    candidate = right_binary_search(left, right, find_target)
    return candidate * candidate == target


def right_binary_search(left: int, right: int, check, *args) -> int:
    """
    Правый бинарный поиск. Задача нахождения последнего подходящего значения
    ---хорошо---|___плохо___
    :param left: указатель на минимальное значение функции
    :param right: указатель на максимальное значение функции
    :param check: функция проверки условия
    :param args: аргументы функции проверки условия
    :return: индекс последнего элемента, удовлетворяющего условию
    """
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, *args):
            left = mid
        else:
            right = mid - 1

    return left


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return is_perfect_square(num)
