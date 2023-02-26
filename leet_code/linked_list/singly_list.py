from dataclasses import dataclass
from typing import Optional


@dataclass
class SinglyListNode:
    """
    Узел двусвязного списка
    """
    val: int
    next: Optional['SinglyListNode'] = None


class SinglyLinkedList:
    """
    Реализация односвязного списка
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def get(self, index: int) -> Optional[SinglyListNode]:
        """ Получение узла по индексу """
        cur = self.head
        idx = 0
        while idx != index:
            if not cur:
                return None

            cur = cur.next
            idx += 1

        return cur

    def add_at_head(self, val: int) -> SinglyListNode:
        """ Добавление в голову """
        cur = SinglyListNode(val)
        cur.next = self.head

        if not self.tail:
            self.tail = cur

        self.head = cur
        self.len += 1

        return cur

    def add_at_tail(self, val: int) -> SinglyListNode:
        """ Добавление в хвост """
        cur = SinglyListNode(val)

        if self.tail:
            self.tail.next = cur
        if not self.head:
            self.head = cur

        self.tail = cur
        self.len += 1

        return cur

    def add_at_index(self, index: int, val: int) -> Optional[SinglyListNode]:
        """ Добавление по индексу """
        if index > self.len:
            return None

        left = self.get(index - 1)
        if not left:
            return self.add_at_head(val)

        right = left.next
        if not right:
            return self.add_at_tail(val)

        cur = SinglyListNode(val)
        cur.next = right
        left.next = cur

        self.len += 1
        return cur

    def delete_at_index(self, index: int) -> None:
        """ Удаление по индексу """
        left = self.get(index - 1)
        if not left:
            return self.delete_at_head()

        curr = left.next
        if not curr:
            return None

        right = curr.next
        if not right:
            return self.delete_at_tail()

        left.next = right
        self.len -= 1

        return None

    def delete_at_head(self) -> None:
        """ Удаление из головы """
        if not self.head:
            return None

        cur = self.head.next
        if not cur:
            # Если в списке один элемент и мы его удаляем
            self.tail = None

        self.head = cur
        self.len -= 1

        return None

    def delete_at_tail(self) -> None:
        """ Удаление с хвоста """
        if not self.tail:
            return None

        if not self.head:
            return None

        cur = self.head
        while cur.next != self.tail:
            cur = cur.next

        self.tail = cur
        self.len -= 1

        return None
