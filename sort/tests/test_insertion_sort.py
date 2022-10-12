from sort.insertion_sort import InsertionSort


def test_main():
    a = [31, 41, 59, 26, 41, 58]

    obj = InsertionSort()

    b = obj.sort(a)
    assert b == [26, 31, 41, 41, 58, 59]


def test_main_1():
    a = [1, 2, 3, 4, 5, 6]

    obj = InsertionSort()

    b = obj.sort(a)
    assert b == [1, 2, 3, 4, 5, 6]


def test_main_2():
    a = [6, 5, 4, 3, 2, 1]

    obj = InsertionSort()

    b = obj.sort(a)
    assert b == [1, 2, 3, 4, 5, 6]


def test_main_3():
    a = [1, 2, 3, 4, 5, 6]

    obj = InsertionSort()

    b = obj.sort(a, reverse=True)
    assert b == [6, 5, 4, 3, 2, 1]
