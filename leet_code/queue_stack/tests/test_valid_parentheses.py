from leet_code.queue_stack.valid_parentheses import Solution


def test_main_1():
    assert Solution().isValid("()")


def test_main_2():
    assert Solution().isValid("()[]{}")


def test_main_3():
    assert not Solution().isValid("(]")


def test_main_4():
    assert Solution().isValid("([{}])")


def test_main_5():
    assert not Solution().isValid("((")

def test_main_6():
    assert not Solution().isValid("){")