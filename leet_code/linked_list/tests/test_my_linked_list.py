from leet_code.linked_list.my_linked_list import DoublyLinkedList
from leet_code.linked_list.singly_list import SinglyLinkedList
from leet_code.linked_list.singly_list2 import MyLinkedList


def test_main_1():
    my_list = DoublyLinkedList()
    my_list.add_at_head(1)
    my_list.add_at_tail(3)
    my_list.add_at_index(1, 2)  # linked list becomes 1->2->3
    assert 2 == my_list.get(1).val  # return 2
    my_list.delete_at_index(1)  # now the linked list is 1->3

    assert 3 == my_list.get(1).val  # return 3

def test_main_2():
    ["MyLinkedList", "addAtHead", "get", "addAtTail", "deleteAtIndex", "get", ]
    [[], [24], [1], [18], [1], [1], ]
    # [null,null,-1,null,null,-1,
    my_list = SinglyLinkedList()
    my_list.add_at_head(1)
    my_list.add_at_tail(3)
    my_list.add_at_index(1, 2)  # linked list becomes 1->2->3
    assert 2 == my_list.get(1).val  # return 2
    my_list.delete_at_index(1)  # now the linked list is 1->3

    assert 3 == my_list.get(1).val  # return 3

def test_main_3():
    my_list = MyLinkedList()
    my_list.addAtHead(24)
    assert -1 == my_list.get(1)
    my_list.addAtTail(18)
    my_list.deleteAtIndex(1)
    assert -1 == my_list.get(1)
