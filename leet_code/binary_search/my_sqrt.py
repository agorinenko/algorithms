import bisect


def test_my_sqrt():
    x = 16
    assert 4 == my_sqrt(x)


def test_my_sqrt_1():
    x = 4
    assert 2 == my_sqrt(x)


def test_my_sqrt_2():
    x = 8
    assert 2 == my_sqrt(x)


def test_my_sqrt_3():
    x = 3
    assert 1 == my_sqrt(x)


def test_my_sqrt_4():
    x = 1
    assert 1 == my_sqrt(x)


def test_left_binary_search():
    # Определяем интервал поиска
    arr = [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Определяем границы нашей функции
    left = 0
    right = len(arr) - 1
    # Искомое число
    target = -2

    def find_target(mid):
        return arr[mid] >= target

    i = left_binary_search(left, right, find_target)
    j = arr[i]
    assert 9 ==i


def test_right_binary_search():
    # Определяем интервал поиска
    arr = [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Определяем границы нашей функции
    left = 0
    right = len(arr) - 1
    # Искомое число
    target = 6

    def find_target(mid):
        return arr[mid] <= target

    assert 9 == right_binary_search(left, right, find_target)


def left_binary_search(left: int, right: int, check, *args) -> int:
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


def my_sqrt(target: int) -> int:
    if target == 1:
        return 1
    left = 0
    right = target - 1

    def find_target(mid):
        return mid * mid <= target

    return right_binary_search(left, right, find_target)


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
    def mySqrt(self, x: int) -> int:
        return my_sqrt(x)
