from typing import List


def test_1():
    assert 1 == Solution().lastStoneWeight([2, 7, 4, 1, 8, 1])


def test_2():
    assert 1 == Solution().lastStoneWeight([1])


def test_3():
    assert 2 == Solution().lastStoneWeight([1, 3])


def test_4():
    assert 0 == Solution().lastStoneWeight([2, 2])


def test_5():
    assert 0 == Solution().lastStoneWeight([2, 6, 6, 9, 4, 3])


def test_6():
    assert 1 == Solution().lastStoneWeight([8, 8, 6, 3, 7, 4, 7])


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaxHeap()
        for stone in stones:
            heap.push(stone)

        while len(heap.heap_list) > 1:
            y = heap.pop()
            x = heap.pop()

            z = abs(y - x)
            if z > 0:
                heap.push(z)

        res = heap.peek()

        return res or z


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
                self.heap_list[cur_idx], self.heap_list[max_child_idx] = self.heap_list[max_child_idx], self.heap_list[cur_idx]
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
