from leet_code.hash_table.contains_duplicate import Solution


def test_main_1():
    s = Solution()
    assert s.contains_duplicate([1, 2, 3, 1])


def test_main_2():
    s = Solution()
    assert not s.contains_duplicate([1, 2, 3, 4])


def test_main_3():
    s = Solution()
    assert s.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
