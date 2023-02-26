from typing import Optional, Tuple


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def get_array_from_list(linked_list: ListNode):
    """
    For debug. Create array from linked list
    :param linked_list: linked list
    :return:
    """
    if not linked_list:
        return []

    a = [linked_list.val]
    while linked_list.next:
        linked_list = linked_list.next
        a.append(linked_list.val)

    return a


def create_list_from_array(a: list) -> ListNode:
    """
    Utils function for tests. Create linked list from array
    :param a: array
    :return: linked list
    """
    pointer_node = None
    head_node = None
    for i, val in enumerate(a):
        if not pointer_node:
            pointer_node = ListNode(val)
            head_node = pointer_node
        else:
            node = ListNode(val)
            pointer_node.next = node
            pointer_node = node
    return head_node


def test_remove_nth_from_end():
    list_1 = create_list_from_array([1, 2, 3, 4, 5])
    result = remove_nth_from_end(list_1, 2)
    arr = get_array_from_list(result)
    assert [1, 2, 3, 5] == arr


def test_remove_nth_from_end_1():
    list_1 = create_list_from_array([1])
    result = remove_nth_from_end(list_1, 1)
    arr = get_array_from_list(result)
    assert [] == arr


def test_remove_nth_from_end_2():
    list_1 = create_list_from_array([1, 2])
    result = remove_nth_from_end(list_1, 1)
    arr = get_array_from_list(result)
    assert [1] == arr


def test_remove_nth_from_end_3():
    list_1 = create_list_from_array([1, 2])
    result = remove_nth_from_end(list_1, 2)
    arr = get_array_from_list(result)
    assert [2] == arr


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head:
        return head

    back_pointer, front_pointer = head, head
    for _ in range(n):
        front_pointer = front_pointer.next

    while front_pointer and front_pointer.next:
        front_pointer = front_pointer.next
        back_pointer = back_pointer.next

    if back_pointer == head and not front_pointer:
        head = head.next
        return head

    if back_pointer == head and not back_pointer.next:
        return None

    back_pointer.next = back_pointer.next.next if back_pointer.next else None

    return head


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return remove_nth_from_end(head, n)
