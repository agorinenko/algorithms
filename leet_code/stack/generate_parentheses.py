from typing import List


def test_1():
    assert set(Solution().generateParenthesis(3)) == {"((()))", "(()())", "(())()", "()(())", "()()()"}


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open_count: int, close_count: int):
            if open_count == n and close_count == n:
                res.append(''.join(stack))
            else:
                if open_count < n:
                    stack.append('(')
                    backtrack(open_count + 1, close_count)
                    stack.pop()

                if close_count < open_count:
                    stack.append(')')
                    backtrack(open_count, close_count + 1)
                    stack.pop()

        backtrack(0, 0)
        return res
