import heapq
from typing import List

def test_1():
    obj = KthLargest(3, [4, 5, 8, 2])
    assert 4 == obj.add(3)
    assert 5 == obj.add(5)
    assert 5 == obj.add(10)
    assert 8 == obj.add(9)
    assert 8 == obj.add(4)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]