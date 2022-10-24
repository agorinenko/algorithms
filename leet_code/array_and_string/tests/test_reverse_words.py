from leet_code.array_and_string.reverse_words import Solution


def test_main_1():
    s = "the sky is blue"
    res = Solution().reverse_words(s)
    assert "blue is sky the" == res


def test_main_2():
    s = "  hello world  "
    res = Solution().reverse_words(s)
    assert "world hello" == res


def test_main_3():
    s = "a good   example"
    res = Solution().reverse_words(s)
    assert "example good a" == res
