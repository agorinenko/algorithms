from leet_code.queue_stack.my_circular_queue import MyCircularQueue


def test_main_1():
    obj = MyCircularQueue(5)
    assert obj.enQueue(1)
    assert not obj.isFull()
    assert obj.deQueue()
    assert obj.isEmpty()

    assert obj.enQueue(1)
    assert obj.enQueue(2)
    assert obj.enQueue(3)
    assert obj.enQueue(4)
    assert obj.enQueue(5)
    assert not obj.enQueue(6)
    assert obj.isFull()
    assert 1 == obj.Front()
    assert 5 == obj.Rear()
    assert obj.deQueue()
    assert 2 == obj.Front()
    assert obj.deQueue()
    assert 3 == obj.Front()
    assert obj.deQueue()
    assert 4 == obj.Front()
    assert obj.deQueue()
    assert 5 == obj.Front()
    assert obj.deQueue()

    assert not obj.deQueue()
