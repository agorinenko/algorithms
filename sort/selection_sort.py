from typing import List


class SelectionSort:
    """
    Сортировка выбором
    Сложность  - O(n^2)
    Находим номер минимального значения в массиве,
    производим обмен этого значения со значением первой неотсортированной позиции
    """

    def sort(self, sequence: List[int], reverse: bool = False) -> List[int]:
        for i, key in enumerate(sequence):
            current_min = key
            current_min_position = i

            from_position = i + 1
            # Ищем минимальное значение в оставшемся "хвосте" массива
            for j, j_key in enumerate(sequence[from_position:]):
                if j_key >= current_min if reverse else j_key < current_min:
                    current_min = j_key
                    current_min_position = from_position + j

            # Производим обмен этого значения со значением первой неотсортированной позиции
            if current_min_position != i:
                tmp = sequence[i]
                sequence[i] = sequence[current_min_position]
                sequence[current_min_position] = tmp

        return sequence
