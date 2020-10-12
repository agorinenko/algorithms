from typing import List


class BubbleSort:
    """
    Сортировка пузырьком
    Сложность  - O(n^2)
    Инвариант: правый хвост
    Устойчив? - Да
    Проходим по массиву до тех пор, пока он не станет отсортирован.
    За каждый проход элементы последовательно сравниваются попарно и, если порядок в паре неверный, выполняется обмен элементов.
    """

    def sort(self, sequence: List[int], reverse: bool = False) -> List[int]:
        _sorted = False
        while not _sorted:
            _sorted = True
            for i, key in enumerate(sequence[:-1]):
                if key < sequence[i + 1] if reverse else key > sequence[i + 1]:
                    tmp = sequence[i]
                    sequence[i] = sequence[i + 1]
                    sequence[i + 1] = tmp
                    _sorted = False

        return sequence
