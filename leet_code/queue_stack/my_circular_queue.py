class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self._len = 0
        self._data = [None for _ in range(k)]
        self._head = -1
        self._tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self._head == -1 and self._tail == -1:
            self._head = 0
            self._tail = 0
        else:
            self._tail += 1

        if self._tail == self.capacity:
            self._tail = 0

        self._len += 1

        self._data[self._tail] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._data[self._head] = None
        self._head += 1
        if self._head == self.capacity:
            self._head = 0
        self._len -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self._data[self._head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self._data[self._tail]

    def isEmpty(self) -> bool:
        return self._len == 0

    def isFull(self) -> bool:
        return self._len == self.capacity
