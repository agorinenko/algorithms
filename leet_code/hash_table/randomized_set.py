import random


class RandomizedSet:

    def __init__(self):
        self.data = set()

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data.add(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data.remove(val)
            return True

        return False

    def getRandom(self) -> int:
        r = random.randint(0, len(self.data) - 1)
        return list(self.data)[r]
