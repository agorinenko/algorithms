from typing import List


def test_remove_element():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert 5 == remove_element(nums, 2)
    print(nums[:5])  # [0, 1, 3, 0, 4]


def remove_element(arr: List[int], val: int):
    """
    Выполняет удаление значение из массива "на месте"
    :param arr: данный массив
    :param val: значение, которое следует удалить
    :return: длинна массива с актуальными значениями
    """
    j = 0  # j is slow runner
    for i in range(len(arr)):  # i is fast runner
        if arr[i] != val:
            arr[j] = arr[i]
            j += 1
    return j
