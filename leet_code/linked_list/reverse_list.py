from typing import Optional


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
    for _, val in enumerate(a):
        if not pointer_node:
            pointer_node = ListNode(val)
            head_node = pointer_node
        else:
            node = ListNode(val)
            pointer_node.next = node
            pointer_node = node
    return head_node


def print_linked_list(linked_list: ListNode):
    """
    For debug. Print linked list
    :param linked_list: linked list
    :return:
    """
    a = get_array_from_list(linked_list) if linked_list else []
    print(a)


def test_reverse_list():
    list_1 = create_list_from_array([1, 2, 3, 4, 5])
    list_1 = reverse_list(list_1)
    assert [5, 4, 3, 2, 1] == get_array_from_list(list_1)


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev_pointer = None
    pointer = head
    while pointer:
        # Create temp pointer on next node
        after_pointer = pointer.next
        # reverse link
        pointer.next = prev_pointer
        # Move prev_pointer and pointer on one step
        prev_pointer = pointer
        pointer = after_pointer

    return prev_pointer


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return reverse_list(head)
