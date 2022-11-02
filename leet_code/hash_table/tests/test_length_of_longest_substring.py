from leet_code.hash_table.length_of_longest_substring import Solution


def test_main_1():
    s = Solution()
    assert s.length_of_longest_substring("abcabcbb") == 3

def test_main_2():
    s = Solution()
    assert s.length_of_longest_substring("bbbbb") == 1

def test_main_3():
    s = Solution()
    assert s.length_of_longest_substring("pwwkew") == 3

def test_main_4():
    s = Solution()
    assert s.length_of_longest_substring(" ") == 1

def test_main_5():
    s = Solution()
    assert s.length_of_longest_substring("au") == 2
