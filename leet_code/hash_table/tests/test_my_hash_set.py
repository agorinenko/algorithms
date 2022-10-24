from leet_code.hash_table.my_hash_set import MyHashSet


def test_main_1():
    my_hash_set = MyHashSet()
    my_hash_set.add(1)  # set = [1]
    my_hash_set.add(2)  # set = [1, 2]
    assert my_hash_set.contains(1)  # return True
    assert not my_hash_set.contains(3)  # return False, (not found)
    my_hash_set.add(2)  # set = [1, 2]
    assert my_hash_set.contains(2)  # return True
    my_hash_set.remove(2)  # set = [1]
    assert not my_hash_set.contains(2)  # return False, (already removed)

def test_main_2():
    my_hash_set = MyHashSet()
    my_hash_set.add(99)  # set = [99]
    assert my_hash_set.contains(99)
    my_hash_set.add(100)  # set = [99, 100]
    assert my_hash_set.contains(100)
    my_hash_set.add(101)  # set = [99, 100, 101]
    assert my_hash_set.contains(101)

def test_main_3():
    my_hash_set = MyHashSet()

    for item in ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]:
        my_hash_set.add(item)
        assert my_hash_set.contains(item)

    for item in ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]:
        my_hash_set.remove(item)
        assert not my_hash_set.contains(item)