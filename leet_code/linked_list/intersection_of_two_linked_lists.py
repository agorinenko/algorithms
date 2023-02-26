from typing import Optional, Tuple


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def print_linked_list(linked_list: ListNode):
    """
    For debug. Print linked list
    :param linked_list: linked list
    :return:
    """
    a = get_array_from_list(linked_list) if linked_list else []
    print(a)


def get_array_from_list(linked_list: ListNode):
    """
    For debug. Create array from linked list
    :param linked_list: linked list
    :return:
    """
    a = [linked_list.val]
    while linked_list.next:
        linked_list = linked_list.next
        a.append(linked_list.val)

    return a


def create_list_from_array(a: list, skip) -> Tuple[ListNode, ListNode]:
    """
    Utils function for tests. Create linked list from array
    :param a: array
    :return: linked list
    """
    pointer_node = None
    head_node = None
    intersection_node = None
    for i, val in enumerate(a):
        if not pointer_node:
            pointer_node = ListNode(val)
            head_node = pointer_node
        else:
            node = ListNode(val)
            pointer_node.next = node
            pointer_node = node
        if i == skip:
            intersection_node = pointer_node

    return head_node, intersection_node


def create_list_from_array2(a: list, intersection_node: ListNode) -> ListNode:
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

    pointer_node.next = intersection_node

    return head_node


def test_intersection():
    list_1, intersection_node = create_list_from_array([4, 1, 8, 4, 5], 2)
    list_2 = create_list_from_array2([5, 6, 1], intersection_node)
    node = get_intersection_node(list_1, list_2)
    idx = str(node) if node else '-1'
    assert '8' == idx


def test_intersection_1():
    # [1, 9, 1, 2, 4]
    # [3, 2, 4]
    list_1, intersection_node = create_list_from_array([1, 9, 1, 2, 4], 3)
    list_2 = create_list_from_array2([3], intersection_node)
    assert get_list_len(list_1) == 5
    assert get_list_len(list_2) == 3
    node = get_intersection_node(list_1, list_2)
    idx = str(node) if node else '-1'
    assert '2' == idx


def get_list_len(l: ListNode) -> int:
    i = 0
    while l:
        i += 1
        l = l.next
    return i


def get_intersection_node(list_1: ListNode, list_2: ListNode) -> Optional[ListNode]:
    if not list_1 or not list_2:
        return None
    list_1_len = get_list_len(list_1)
    list_2_len = get_list_len(list_2)
    diff = list_2_len - list_1_len
    i = 0
    if diff > 0:
        # второй больше первого
        while i < diff:
            i += 1
            list_2 = list_2.next
    elif diff < 0:
        # первый больше второго
        diff = abs(diff)
        while i < diff:
            i += 1
            list_1 = list_1.next

    while list_1 or list_2:
        if list_1 and list_2 and id(list_1) == id(list_2):
            return list_1

        if list_1:
            list_1 = list_1.next

        if list_2:
            list_2 = list_2.next

    return None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        return get_intersection_node(headA, headB)
