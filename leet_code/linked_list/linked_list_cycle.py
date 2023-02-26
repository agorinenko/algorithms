from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
            pointer_node = ListNode(val)
            head_node = pointer_node
        else:
            node = ListNode(val)
            pointer_node.next = node
            pointer_node = node
        if i == pos:
            cycle_node = pointer_node

    if cycle_node:
        pointer_node.next = cycle_node

    return head_node


def iterate_by_list(linked_list: ListNode):
    """
    Iterate by
    :param linked_list: linked list and return prev and next nodes for step
    :return:
    """
    prev_node = None
    next_node = linked_list
    yield prev_node, next_node

    while next_node.next:
        prev_node = next_node
        next_node = next_node.next
        yield prev_node, next_node


def test_has_cycle():
    list_1 = create_list_from_array([3, 2, 0, -4], 1)

    assert has_cycle(list_1)


def has_cycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False

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
            return True

    return False


def test_main_2():
    list_1 = create_list_from_array([1, 2], 0)

    assert Solution().hasCycle(list_1)


def test_main_3():
    list_1 = create_list_from_array([1], -1)

    assert not Solution().hasCycle(list_1)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

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
                return True

        return False
