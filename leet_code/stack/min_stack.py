"""
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/
"""
from collections import deque


class MyStack:

    def __init__(self):
        self.deque = deque()

    def push(self, x: int) -> None:
        self.deque.append(x)
        s = len(self.deque)
        while s > 1:
            self.deque.append(self.deque.popleft())
            s -= 1

    def pop(self) -> int:
        return self.deque.popleft()

    def top(self) -> int:
        return self.deque[0]

    def empty(self) -> bool:
        return len(self.deque) == 0


class MinStack:
    """
    Реализация стека на основе динамического массива
    """

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
