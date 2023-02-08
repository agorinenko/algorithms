from leet_code.linked_list.my_linked_list import MyLinkedList


def test_main_1():
    my_list = MyLinkedList()
    my_list.addAtHead(1)
    my_list.addAtTail(3)
    my_list.addAtIndex(1, 2)
    my_list.get(1)
    my_list.deleteAtIndex(1)

    my_list.get(1)