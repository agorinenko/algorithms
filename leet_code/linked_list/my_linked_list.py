"""
DoublyLinkedList
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class DoublyListNode:
    """
    Узел двусвязного списка
    """
    val: int
    prev: Optional['DoublyListNode'] = None
    next: Optional['DoublyListNode'] = None


class DoublyLinkedList:
    """
    Реализация двусвязного списка
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def get(self, index: int) -> Optional[DoublyListNode]:
        """ Получение узла по индексу """
        cur = self.head
        idx = 0
        while idx != index:
            if not cur:
                return None

            cur = cur.next
            idx += 1

        return cur

    def add_at_head(self, val: int) -> DoublyListNode:
        """ Добавление в голову """
        cur = DoublyListNode(val)
        cur.next = self.head
        if self.head:
            self.head.prev = cur
        if not self.tail:
            self.tail = cur

        self.head = cur
        self.len += 1

        return cur

    def add_at_tail(self, val: int) -> DoublyListNode:
        """ Добавление в хвост """
        cur = DoublyListNode(val)
        cur.prev = self.tail
        if self.tail:
            self.tail.next = cur
        if not self.head:
            self.head = cur

        self.tail = cur
        self.len += 1

        return cur

    def add_at_index(self, index: int, val: int) -> Optional[DoublyListNode]:
        """ Добавление по индексу """
        if index > self.len:
            return None

        right = self.get(index)
        if not right:
            return self.add_at_tail(val)

        left = right.prev
        if not left:
            return self.add_at_head(val)

        cur = DoublyListNode(val)
        cur.prev = left
        cur.next = right
        left.next = cur
        right.prev = cur
        self.len += 1
        return cur

    def delete_at_index(self, index: int) -> None:
        """ Удаление по индексу """
        curr = self.get(index)
        if not curr:
            return None

        left = curr.prev
        right = curr.next

        if not left:
            return self.delete_at_head()

        if not right:
            return self.delete_at_tail()

        right.prev = left
        left.next = right
        self.len -= 1

        return None

    def delete_at_head(self) -> None:
        """ Удаление из головы """
        if not self.head:
            return None

        cur = self.head.next
        if cur:
            cur.prev = None
        else:
            # Если в списке один элемент и мы его удаляем
            self.tail = None

        self.head = cur
        self.len -= 1

        return None

    def delete_at_tail(self) -> None:
        """ Удаление с хвоста """
        if not self.tail:
            return None

        cur = self.tail.prev
        if cur:
            cur.next = None
        else:
            # Если в списке один элемент и мы его удаляем
            self.head = None

        self.tail = cur
        self.len -= 1

        return None
