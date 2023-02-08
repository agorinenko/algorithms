"""
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1361/
"""


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
