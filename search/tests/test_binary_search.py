from search.binary_search import BinarySearch


def test_main_1():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert 0 == BinarySearch().search(nums, 1)
    assert 4 == BinarySearch().search(nums, 5)
    assert 5 == BinarySearch().search(nums, 6)
    assert 9 == BinarySearch().search(nums, 10)
    assert -1 == BinarySearch().search(nums, 11)

def test_main_2():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert 0 == BinarySearch().search(nums, 1)
    assert 4 == BinarySearch().search(nums, 5)
    assert 5 == BinarySearch().search(nums, 6)
    assert 9 == BinarySearch().search(nums, 10)
    assert -1 == BinarySearch().search(nums, 12)

def test_main_3():
    nums = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
    assert 0 == BinarySearch().search(nums, 1)
    assert 4 == BinarySearch().search(nums, 5)
    assert 5 == BinarySearch().search(nums, 6)
    assert 10 == BinarySearch().search(nums, 10)
    assert -1 == BinarySearch().search(nums, 12)