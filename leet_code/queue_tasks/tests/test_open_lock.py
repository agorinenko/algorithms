from leet_code.queue_stack.open_lock import Solution


def test_main_1():
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    assert Solution().openLock(deadends, target) == 6


def test_main_2():
    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"
    assert Solution().openLock(deadends, target) == -1


def test_main_3():
    deadends = ["8888"]
    target = "0009"
    assert Solution().openLock(deadends, target) == 1
