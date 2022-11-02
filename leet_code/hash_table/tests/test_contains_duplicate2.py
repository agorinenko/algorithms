from leet_code.hash_table.contains_duplicate2 import Solution


def test_main_1():
    s = Solution()
    assert s.contains_nearby_duplicate([1, 2, 3, 1], 3)


def test_main_2():
    s = Solution()
    assert s.contains_nearby_duplicate([1, 0, 1, 1], 1)


def test_main_3():
    s = Solution()
    assert not s.contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2)
