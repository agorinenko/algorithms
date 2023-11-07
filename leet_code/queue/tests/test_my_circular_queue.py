from leet_code.queue_stack.my_circular_queue import MyCircularQueue


def test_main_1():
    obj = MyCircularQueue(5)
    assert obj.enqueue(1)
    assert not obj.is_full()
    assert obj.dequeue()
    assert obj.is_empty()

    assert obj.enqueue(1)
    assert obj.enqueue(2)
    assert obj.enqueue(3)
    assert obj.enqueue(4)
    assert obj.enqueue(5)
    assert not obj.enqueue(6)
    assert obj.is_full()
    assert 1 == obj.front()
    assert 5 == obj.rear()
    assert obj.dequeue()
    assert 2 == obj.front()
    assert obj.dequeue()
    assert 3 == obj.front()
    assert obj.dequeue()
    assert 4 == obj.front()
    assert obj.dequeue()
    assert 5 == obj.front()
    assert obj.dequeue()

    assert not obj.dequeue()
