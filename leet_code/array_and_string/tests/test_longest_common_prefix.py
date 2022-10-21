from leet_code.array_and_string.longest_common_prefix import Solution


def test_main_1():
    res = Solution().longest_common_prefix(["flower", "flow", "flight"])
    assert 'fl' == res


def test_main_2():
    res = Solution().longest_common_prefix(["dog", "racecar", "car"])
    assert '' == res


def test_main_3():
    res = Solution().longest_common_prefix(["reflower","flow","flight"])
    assert '' == res