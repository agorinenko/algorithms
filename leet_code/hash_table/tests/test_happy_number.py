from leet_code.hash_table.happy_number import Solution


def test_main_1():
    s = Solution()
    assert s.is_happy(19)

def test_main_2():
    s = Solution()
    assert not s.is_happy(2)

def test_main_3():
    s = Solution()
    assert s.is_happy(7)

def test_main_4():
    s = Solution()
    assert s.is_happy(1111111)