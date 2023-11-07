"""
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1361/
"""
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

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        open_chars = ['(', '[', '{']
        close_chars = [')', ']', '}']
        m = {
            ')': '(', ']': '[', '}': '{'
        }
        for parenthese in s:
            if parenthese in open_chars:
                stack.append(parenthese)
            elif parenthese in close_chars:
                if not stack:
                    return False
                top = stack[-1]
                if top == m[parenthese]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
