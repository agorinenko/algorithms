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


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def get(self, index: int) -> int:
        cur = self.head
        idx = 0
        while idx != index:
            if not cur:
                return -1

            cur = cur.next
            idx += 1

        return cur

    def addAtHead(self, val: int) -> None:
        pass

    def addAtTail(self, val: int) -> None:
        pass

    def addAtIndex(self, index: int, val: int) -> None:
        pass

    def deleteAtIndex(self, index: int) -> None:
        pass
