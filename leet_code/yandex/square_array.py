from typing import List


def test_1():
    arr = [-5, -4, 1, 2, 3, 4, 5]

    assert solution(arr) == [1, 4, 9, 16, 16, 25, 25]


def test_2():
    assert solution([]) == []
    assert solution([2]) == [4]
    assert solution([1, 2]) == [1, 4]


def solution(arr: List[int]) -> List[int]:
    f, s = -1, 0
    for i in range(len(arr)):
        if i > 0 and arr[i - 1] < 0 <= arr[i]:
            f = i - 1
            s = i
            break

    result = []
    while f >= 0 or s < len(arr):
        if s >= len(arr):
            l_val = arr[f] ** 2
            result.append(l_val)
            f -= 1
        elif f < 0:
            r_val = arr[s] ** 2
            result.append(r_val)
            s += 1
        else:
            r_val = arr[s] ** 2
            l_val = arr[f] ** 2
            if r_val < l_val:
                result.append(r_val)
                s += 1
            else:
                result.append(l_val)
                f -= 1
                
    return result
