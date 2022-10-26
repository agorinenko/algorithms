class BinarySearch:
    def search(self, arr: list[int], value: int) -> int:
        """
        Двоичный (бинарный) поиск (дихотомия)
        :param arr: массив для поиска.
        :param value: элемент, который нужно найти.
        :return: индекс элемента или -1 если не найдено
        """
        left = 0
        right = len(arr) - 1
        while left <= right:
            middle_idx = (left + right) // 2
            middle = arr[middle_idx]
            if middle < value:
                left = middle_idx + 1
            elif middle > value:
                right = middle_idx - 1
            else:
                return middle_idx
        return -1
