from typing import List


class InsertionSort:
    """
    Сортировка вставкой
    Сложность  - O(n^2)
    Массив разбивается на отсортированную последовательность слева и то, что надо отсортировать справа
    """

    def sort(self, sequence: List[int], reverse: bool = False) -> List[int]:
        j = 1
        for key in sequence[j:]:
            i = j - 1
            # вставляем  sequence[j] в отсортированную последовательность слева
            while i >= 0 and (sequence[i] < key if reverse else sequence[i] > key):
                sequence[i + 1] = sequence[i]
                i -= 1

            sequence[i + 1] = key
            j += 1

        return sequence
