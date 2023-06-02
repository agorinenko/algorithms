from typing import Optional


class MyCircularQueue:
    """
    Реализация очереди в виде кольцевого буфера
    """
    def __init__(self, k: int):
        """
        Очередь
        :param k: максимальный размер очереди
        """
        self.capacity = k
        self._len = 0
        self._data = [None for _ in range(k)]
        self._head = -1
        self._tail = -1

    def enqueue(self, value: int) -> bool:
        """
        Операция вставки всегда добавляет новый элемент в конец очереди
        :param value: элемент для вставки
        :return: True, если операция успешна
        """
        if self.is_full():
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

    def dequeue(self) -> bool:
        """
        Операция удаления всегда удаляет элемент из начала очереди.
        :return: True, если операция успешна
        """
        if self.is_empty():
            return False

        self._data[self._head] = None
        self._head += 1

        if self._head == self.capacity:
            self._head = 0

        self._len -= 1

        return True

    def front(self) -> Optional[int]:
        """
        Получение элемента из головы
        :return: элемент
        """
        if self.is_empty():
            return None

        return self._data[self._head]

    def rear(self) -> Optional[int]:
        """
        Получение элемента из хвоста
        :return:
        """
        if self.is_empty():
            return None

        return self._data[self._tail]

    def is_empty(self) -> bool:
        """
        Очередь пуста.
        :return: True, если очередь пуста.
        """
        return self._len == 0

    def is_full(self) -> bool:
        """
        Очередь заполнена.
        :return: True, если очередь заполнена.
        """
        return self._len == self.capacity
