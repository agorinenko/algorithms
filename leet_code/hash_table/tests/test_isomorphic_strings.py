from leet_code.hash_table.isomorphic_strings import Solution


def test_main_1():
    s = Solution()
    assert not s.is_isomorphic("badc", "baba")


def test_main_2():
    s = Solution()
    assert s.is_isomorphic("egg", "add")

def test_main_3():
    s = Solution()
    assert not s.is_isomorphic("foo", "bar")
