from typing import Optional


class ListNode:
    def __init__(self, x, idx=None):
        self.val = x
        self.next = None
        self.idx = idx

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def create_list_from_array(a: list, pos) -> ListNode:
    """
    Utils function for tests. Create linked list from array
    :param a: array
    :return: linked list
    """
    pointer_node = None
    head_node = None
    cycle_node = None
    for i, val in enumerate(a):
        if not pointer_node:
            pointer_node = ListNode(val, idx=i)
            head_node = pointer_node
        else:
            node = ListNode(val, idx=i)
            pointer_node.next = node
            pointer_node = node
        if i == pos:
            cycle_node = pointer_node

    if cycle_node:
        pointer_node.next = cycle_node

    return head_node


def test_detect_cycle():
    list_1 = create_list_from_array([3, 2, 0, -4, 5, 6], 3)
    node = detect_cycle(list_1)
    idx = node.idx if node else -1
    assert idx == 3


def test_detect_cycle_1():
    list_1 = create_list_from_array([1, 2], 0)
    node = detect_cycle(list_1)
    idx = node.idx if node else -1
    assert idx == 0


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    first_pointer = head
    second_pointer = head

    while True:
        # move slow pointer one step each time
        first_pointer = first_pointer.next
        # move fast pointer two steps each time
        second_pointer = second_pointer.next
        if not second_pointer:
            break
        second_pointer = second_pointer.next
        if not second_pointer:
            break

        # change this condition to fit specific problem
        if id(first_pointer) == id(second_pointer):
            while first_pointer != head:
                first_pointer, head = first_pointer.next, head.next
            return first_pointer

    return None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return detect_cycle(head)
