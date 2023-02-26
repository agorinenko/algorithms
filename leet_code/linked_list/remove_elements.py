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


def test_remove_elements():
    list_1 = create_list_from_array([1, 2, 6, 3, 4, 5, 6])
    list_1 = remove_elements(list_1, 6)
    arr = get_array_from_list(list_1)
    assert arr == [1, 2, 3, 4, 5]


def test_remove_elements_1():
    list_1 = create_list_from_array([7, 7, 7, 7])
    list_1 = remove_elements(list_1, 7)
    arr = get_array_from_list(list_1)
    assert arr == []


def test_remove_elements_2():
    list_1 = create_list_from_array([7, 6, 7, 6, 7])
    list_1 = remove_elements(list_1, 7)
    arr = get_array_from_list(list_1)
    assert arr == [6, 6]


def test_remove_elements_3():
    list_1 = create_list_from_array([1])
    list_1 = remove_elements(list_1, 2)
    arr = get_array_from_list(list_1)
    assert arr == [1]


def test_remove_elements_4():
    list_1 = create_list_from_array([1])
    list_1 = remove_elements(list_1, 1)
    arr = get_array_from_list(list_1)
    assert arr == []


def test_remove_elements_5():
    list_1 = create_list_from_array([1, 2])
    list_1 = remove_elements(list_1, 1)
    arr = get_array_from_list(list_1)
    assert arr == [2]


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head:
        return head

    prev = ListNode(0)
    prev.next = head
    curr = head

    is_set_head = False
    is_find = False

    while curr.next:
        if curr.val == val:
            is_find = True
            prev.next = curr.next
        else:
            if not is_set_head:
                head = curr
                is_set_head = True
            prev = curr
        curr = curr.next

    if curr.val == val:
        is_find = True
        prev.next = None
    else:
        if not is_set_head:
            head = curr
            is_set_head = True

    if not is_set_head and is_find:
        return None

    return head


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        return remove_elements(head, val)
