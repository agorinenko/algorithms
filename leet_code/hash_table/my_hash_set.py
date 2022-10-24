from typing import Optional, Any


class MyHashSet:
    def __init__(self):
        self._per_page = 100
        self._current_page = 0
        self._data = []
        self._extend_data_if_need()

    def add(self, key: Any) -> None:
        bucket = self._get_bucket(key)
        if not self.contains(key):
            bucket.append(key)

    def remove(self, key: Any) -> None:
        bucket = self._get_bucket(key)
        if self.contains(key):
            bucket.remove(key)

    def contains(self, key: Any) -> bool:
        bucket = self._get_bucket(key)
        for i in bucket:
            if i == key:
                return True

        return False

    def _extend_data_if_need(self, position: Optional[int] = 0):
        position_page = (position // self._per_page) + 1
        if position_page > self._current_page:
            extend_count = (position_page - self._current_page) * self._per_page
            extend_list = [[] for _ in range(extend_count)]
            self._data.extend(extend_list)
            self._current_page = position_page

    def _get_bucket(self, key: Any) -> list:
        """
         Return bucket for the hash value for the given object.

        Two objects that compare equal must also have the same hash value, but the reverse is not necessarily true.
        """
        bucket_idx = abs(hash(key)) % (10 ** 6)
        self._extend_data_if_need(bucket_idx)

        return self._data[bucket_idx]

    def __str__(self):
        return str(self._data)
