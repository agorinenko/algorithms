from typing import Optional, Callable, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def find_nodes_range(linked_list: ListNode, filter_func: Callable) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    """
    Find range of nodes for filter
    :param linked_list: linked list
    :param filter_func: filter function, for example, "lambda node: node.val <= next_node.val"
    :return: first and last nodes of range. (None, None) if range not found and (first_node, None) if found only one node
    """
    last_node = None
    first_node = None
    if filter_func(linked_list):
        last_node = linked_list
        first_node = linked_list

    while linked_list.next:
        linked_list = linked_list.next
        if filter_func(linked_list):
            last_node = linked_list
            if not first_node:
                first_node = linked_list

    if id(first_node) == id(last_node):
        return first_node, None

    return first_node, last_node


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
    prev_node = None
    next_node = linked_list
    yield prev_node, next_node

    while next_node.next:
        prev_node = next_node
        next_node = next_node.next
        yield prev_node, next_node


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

        # Iterate by list2
        i = 1

        for prev_node, next_node in iterate_by_list(list_2):
            # if empty list
            if not list_1:
                break

            # find in list1 range of nodes with val <= next_node.val
            first_node, last_node = find_nodes_range(list_1, lambda node: node.val <= next_node.val)
            # if find nodes
            if first_node:
                # set list1 head
                list_1 = last_node.next if last_node else first_node.next

                # move list1 range of nodes to list2
                if not prev_node:
                    # first iterate step and find range
                    if last_node:
                        last_node.next = next_node
                    else:
                        first_node.next = next_node
                    list_2 = first_node
                else:
                    prev_node.next = first_node

                if last_node:
                    last_node.next = next_node
                else:
                    first_node.next = next_node
            print(f'======={i}========')
            print('list 1')
            print_linked_list(list_1)
            print('list 2')
            print_linked_list(list_2)
            i += 1

        # list2 iterated but list 1 is not empty
        if list_1:
            next_node.next = list_1

        return list_2
