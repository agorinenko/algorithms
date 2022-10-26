from leet_code.hash_table.two_sum import Solution


def test_main_1():
    s = Solution()
    assert [0, 1] == s.two_sum([2, 7, 11, 15], 9)


def test_main_2():
    s = Solution()
    assert [1, 2] == s.two_sum([3, 2, 4], 6)


def test_main_3():
    s = Solution()
    assert [0, 1] == s.two_sum([3, 3], 6)
