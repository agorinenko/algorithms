from typing import Optional


class DoublyListNode:
    """
    Узел двусвязного списка
    """

    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.get_node(index)

        return cur.val if cur else -1

    def get_node(self, index: int) -> Optional[DoublyListNode]:
        cur = self.head
        idx = 0
        while idx != index:
            if not cur:
                return None

            cur = cur.next
            idx += 1

        return cur

    def addAtHead(self, val: int) -> None:
        node = DoublyListNode(val)
        node.next = self.head
        if self.head:
            self.head.prev = node
        if not self.tail:
            self.tail = node

        self.head = node

    def addAtTail(self, val: int) -> None:
        node = DoublyListNode(val)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        if not self.head:
            self.head = node

        self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        right = self.get_node(index)
        if not right:
            return self.addAtTail(val)

        left = right.prev
        if not left:
            return self.addAtHead(val)

        cur = DoublyListNode(val)
        cur.prev = left
        cur.next = right
        left.next = cur
        right.prev = cur

    def deleteAtIndex(self, index: int) -> None:
        curr = self.get_node(index)
        if not curr:
            return None

        right = curr.next
        left = curr.prev
        left.next  = right
        right.prev = left
