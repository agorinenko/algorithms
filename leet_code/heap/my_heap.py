def test_push():
    heap = MinHeap()

    heap.push(2)
    heap.push(5)
    heap.push(4)
    heap.push(11)
    heap.push(6)
    heap.push(8)
    heap.push(25)
    heap.push(12)
    heap.push(20)

    assert heap.heap_list == [2, 5, 4, 11, 6, 8, 25, 12, 20]

    heap.push(3)

    assert heap.heap_list == [2, 3, 4, 11, 5, 8, 25, 12, 20, 6]


def test_peek():
    heap = MinHeap()
    heap.push(5)
    heap.push(4)
    heap.push(11)
    heap.push(6)
    heap.push(8)
    heap.push(25)
    heap.push(12)
    heap.push(20)
    heap.push(3)
    heap.push(2)

    assert 2 == heap.peek()


def test_pop():
    heap = MinHeap()

    heap.push(2)
    heap.push(5)
    heap.push(4)
    heap.push(11)
    heap.push(6)
    heap.push(8)
    heap.push(25)
    heap.push(12)
    heap.push(20)

    assert heap.heap_list == [2, 5, 4, 11, 6, 8, 25, 12, 20]

    assert 2 == heap.pop()

    assert heap.heap_list == [4, 5, 8, 11, 6, 20, 25, 12]


class MinHeap:
    """ Реализация кучи минимумов на python с использованием массива """

    def __init__(self):
        self.heap_list = []

    def is_empty(self):
        return not bool(self.heap_list)

    def push(self, key: int):
        """ Добавление в кучу """
        self.heap_list.append(key)
        cur_idx = len(self.heap_list) - 1
        while cur_idx > 0 and self.heap_list[cur_idx] < self._get_parent(cur_idx):
            parent_idx = _get_parent_index(cur_idx)
            # Меняем текущий элемент с родителем
            self.heap_list[cur_idx], self.heap_list[parent_idx] = self.heap_list[parent_idx], self.heap_list[cur_idx]
            cur_idx = parent_idx

    def peek(self):
        """ Получение минимума """
        if len(self.heap_list) > 0:
            return self.heap_list[0]

        return None

    def pop(self):
        """ Извлечение с вершины кучи """
        if len(self.heap_list) == 1:
            return self.heap_list.pop()

        result = self.peek()
        # Берем самый правый в последнем ряду элемент и переносим его на место удаляемого элемента
        self.heap_list[0] = self.heap_list.pop()
        cur_idx = 0

        while True:
            max_idx = len(self.heap_list) - 1

            left_idx = _get_left_child_index(cur_idx)
            right_idx = _get_right_child_index(cur_idx)

            if left_idx > max_idx and right_idx > max_idx:
                #  Если после перестановки у просеиваемого элемента нет сыновей, то завершаем алгоритм
                break

            if left_idx <= max_idx and right_idx <= max_idx:
                # Если у просеиваемого элемента два сына
                max_child_idx = left_idx if self.heap_list[left_idx] < self.heap_list[right_idx] else right_idx
            elif left_idx <= max_idx:
                max_child_idx = left_idx
            else:
                max_child_idx = right_idx

            if self.heap_list[max_child_idx] < self.heap_list[cur_idx]:
                self.heap_list[cur_idx], self.heap_list[max_child_idx] = self.heap_list[max_child_idx], self.heap_list[
                    cur_idx]
                cur_idx = max_child_idx
            else:
                break

        return result

    def _get_parent(self, idx: int) -> int:
        """ Получение родительского ключа """
        parent_idx = _get_parent_index(idx)
        return self.heap_list[parent_idx]

    def __str__(self):
        return str(self.heap_list)


class MaxHeap:
    """ Реализация кучи максимума на python с использованием массива """

    def __init__(self):
        self.heap_list = []

    def is_empty(self):
        return not bool(self.heap_list)

    def push(self, key: int):
        """ Добавление в кучу """
        self.heap_list.append(key)
        cur_idx = len(self.heap_list) - 1
        while cur_idx > 0 and self.heap_list[cur_idx] > self._get_parent(cur_idx):
            parent_idx = _get_parent_index(cur_idx)
            # Меняем текущий элемент с родителем
            self.heap_list[cur_idx], self.heap_list[parent_idx] = self.heap_list[parent_idx], self.heap_list[cur_idx]
            cur_idx = parent_idx

    def peek(self):
        """ Получение минимума """
        if len(self.heap_list) > 0:
            return self.heap_list[0]

        return None

    def pop(self):
        """ Извлечение с вершины кучи """
        if len(self.heap_list) == 1:
            return self.heap_list.pop()

        result = self.peek()
        # Берем самый правый в последнем ряду элемент и переносим его на место удаляемого элемента
        self.heap_list[0] = self.heap_list.pop()
        cur_idx = 0

        while True:
            max_idx = len(self.heap_list) - 1

            left_idx = _get_left_child_index(cur_idx)
            right_idx = _get_right_child_index(cur_idx)

            if left_idx > max_idx and right_idx > max_idx:
                #  Если после перестановки у просеиваемого элемента нет сыновей, то завершаем алгоритм
                break

            if left_idx <= max_idx and right_idx <= max_idx:
                # Если у просеиваемого элемента два сына
                max_child_idx = left_idx if self.heap_list[left_idx] > self.heap_list[right_idx] else right_idx
            elif left_idx <= max_idx:
                max_child_idx = left_idx
            else:
                max_child_idx = right_idx

            if self.heap_list[max_child_idx] > self.heap_list[cur_idx]:
                self.heap_list[cur_idx], self.heap_list[max_child_idx] = self.heap_list[max_child_idx], self.heap_list[
                    cur_idx]
                cur_idx = max_child_idx
            else:
                break

        return result

    def _get_parent(self, idx: int) -> int:
        """ Получение родительского ключа """
        parent_idx = _get_parent_index(idx)
        return self.heap_list[parent_idx]

    def __str__(self):
        return str(self.heap_list)


def _get_parent_index(i: int) -> int:
    """ Индекс родителя """
    return (i - 1) // 2


def _get_left_child_index(i: int) -> int:
    """ Индекс левого ребенка """
    return 2 * i + 1


def _get_right_child_index(i: int) -> int:
    """ Индекс правого ребенка """
    return 2 * i + 2
