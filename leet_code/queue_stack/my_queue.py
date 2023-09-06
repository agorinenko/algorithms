class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.auxiliary_stack = []

    def push(self, x: int) -> None:
        while self.main_stack:
            self.auxiliary_stack.append(self.main_stack.pop())

        self.main_stack.append(x)

        while self.auxiliary_stack:
            self.main_stack.append(self.auxiliary_stack.pop())


    def pop(self) -> int:
        return self.main_stack.pop()

    def peek(self) -> int:
        return self.main_stack[-1]

    def empty(self) -> bool:
        return  len(self.main_stack) == 0