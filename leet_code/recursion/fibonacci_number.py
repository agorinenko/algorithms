from typing import Optional


class Solution:
    memory = {}

    def fib(self, n: int) -> int:
        if n in self.memory:
            return self.memory[n]

        if n == 0:
            self.memory[0] = 0

            return 0
        if n == 1:
            self.memory[1] = 1
            return 1

        result = self.fib(n - 1) + self.fib(n - 2)
        self.memory[n] = result
        return result
