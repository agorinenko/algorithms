"""
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/
"""


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
            return

        (num, min_num) = self.stack[-1]
        if val < min_num:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min_num))
        return

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        (num, _) = self.stack[-1]
        return num

    def getMin(self) -> int:
        (_, min_num) = self.stack[-1]
        return min_num
