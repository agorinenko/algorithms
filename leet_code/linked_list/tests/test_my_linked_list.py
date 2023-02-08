from leet_code.linked_list.my_linked_list import DoublyLinkedList


def test_main_1():
    my_list = DoublyLinkedList()
    my_list.add_at_head(1)
    my_list.add_at_tail(3)
    my_list.add_at_index(1, 2)  # linked list becomes 1->2->3
    assert 2 == my_list.get(1).val  # return 2
    my_list.delete_at_index(1)  # now the linked list is 1->3

    assert 3 == my_list.get(1).val  # return 3