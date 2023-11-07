import itertools
from typing import List, Tuple


def test_1():
    assert set(Solution().generateParenthesis(3)) == {"((()))", "(()())", "(())()", "()(())", "()()()"}


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = ['('] * n + [')'] * n
        perms = itertools.permutations(arr)
        res = set()
        for perm in perms:
            if perm not in res and is_valid(perm):
                res.add(perm)

        return [''.join(p) for p in res ]


def is_valid(s: Tuple[str]) -> bool:
    if len(s) <= 1:
        return False

    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False

            if stack[-1] == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0
