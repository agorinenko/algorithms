from typing import List


def test_main_1():
    tokens = ["2", "1", "+", "3", "*"]
    assert 9 == Solution().evalRPN(tokens)


def test_main_2():
    tokens = ["4", "13", "5", "/", "+"]
    assert 6 == Solution().evalRPN(tokens)


def test_main_3():
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert 22 == Solution().evalRPN(tokens)

def test_main_4():
    tokens = ["18"]
    assert 18 == Solution().evalRPN(tokens)


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()

                c = int(eval(f'{b}{token}{a}'))

                stack.append(c)
            else:
                stack.append(token)

        return int(stack.pop())
