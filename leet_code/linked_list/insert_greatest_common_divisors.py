# Definition for singly-linked list.
import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def create_list_from_array(a: list) -> ListNode:
    """
    Utils function for tests. Create linked list from array
    :param a: array
    :return: linked list
    """
    pointer_node = None
    head_node = None
    for val in a:
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


def iterate_by_list(linked_list: ListNode):
    """
    Iterate by
    :param linked_list: linked list and return prev and next nodes for step
    :return:
    """
    # prev_node = None
    # next_node = linked_list
    # yield prev_node, next_node

    while linked_list.next:
        prev_node = linked_list
        linked_list = linked_list.next
        yield prev_node, linked_list


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            for prev_node, next_node in iterate_by_list(head):
                if prev_node and next_node:
                    gcd = math.gcd(prev_node.val, next_node.val)
                    node = ListNode(val=gcd, next=next_node)
                    prev_node.next = node

        return head


def test_main_1():
    list_1 = create_list_from_array([18, 6, 10, 3])

    list_2 = Solution().insertGreatestCommonDivisors(list_1)
    a = get_array_from_list(list_2)
    assert [18, 6, 6, 2, 10, 1, 3] == a
