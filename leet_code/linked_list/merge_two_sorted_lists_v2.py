from typing import Optional, Callable, Tuple


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
    a.sort()
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


def test_main_1():
    list_1 = create_list_from_array([1, 1, 2, 2, 4, 4])
    list_2 = create_list_from_array([1, 3, 4])
    list_3 = Solution().mergeTwoLists(list_1, list_2)
    a = get_array_from_list(list_3)
    assert [1, 1, 1, 2, 2, 3, 4, 4, 4] == a


def test_main_2():
    list_1 = create_list_from_array([1, 2, 4])
    list_2 = create_list_from_array([1, 3, 4])

    list_3 = Solution().mergeTwoLists(list_1, list_2)

    a = get_array_from_list(list_3)
    assert [1, 1, 2, 3, 4, 4] == a


def test_main_3():
    list_1 = create_list_from_array([1])
    list_2 = create_list_from_array([])

    list_3 = Solution().mergeTwoLists(list_1, list_2)

    a = get_array_from_list(list_3)
    assert [1] == a


def test_main_4():
    list_1 = create_list_from_array([3, 4])
    list_2 = create_list_from_array([1, 2])

    list_3 = Solution().mergeTwoLists(list_1, list_2)

    a = get_array_from_list(list_3)
    assert [1, 2, 3, 4] == a


class Solution:
    def mergeTwoLists(self, list_1: Optional[ListNode], list_2: Optional[ListNode]) -> Optional[ListNode]:
        if not list_1:
            return list_2
        if not list_2:
            return list_1

        merged_list = ListNode()
        merged_list_ptr = None
        list_1_ptr = list_1
        list_2_ptr = list_2

        while list_1_ptr and list_2_ptr:
            if list_1_ptr.val < list_2_ptr.val:
                node = ListNode(val=list_1_ptr.val)
                list_1_ptr = list_1_ptr.next
            else:
                node = ListNode(val=list_2_ptr.val)
                list_2_ptr = list_2_ptr.next

            if merged_list_ptr:
                merged_list_ptr.next = node
                merged_list_ptr = node
            else:
                merged_list_ptr = node
                merged_list.next = merged_list_ptr

        while list_1_ptr:
            node = ListNode(val=list_1_ptr.val)

            merged_list_ptr.next = node
            merged_list_ptr = node

            list_1_ptr = list_1_ptr.next

        while list_2_ptr:
            node = ListNode(val=list_2_ptr.val)

            merged_list_ptr.next = node
            merged_list_ptr = node

            list_2_ptr = list_2_ptr.next

        return merged_list.next
