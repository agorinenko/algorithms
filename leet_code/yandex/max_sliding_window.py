import heapq
from collections import deque
from typing import List


def test_1():
    arr = [6, 2, 3, 7, 0, 1]
    k = 3

    assert Solution().maxSlidingWindow(arr, k) == [6, 7, 7, 7]


def test_2():
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    assert Solution().maxSlidingWindow(arr, k) == [3, 3, 5, 5, 6, 7]


def test_3():
    arr = [1, -1]
    k = 1

    assert Solution().maxSlidingWindow(arr, k) == [1, -1]


def test_4():
    arr = [6, 2, 3, 7, 0, 1]
    k = 2

    assert Solution().maxSlidingWindow(arr, k) == [6, 3, 7, 7, 1]


class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        maxHeap, res = [], []
        for i in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))
            if i >= k - 1:
                while maxHeap[0][1] <= i - k:  # this is because the highest one is not in the window range
                    heapq.heappop(maxHeap)
                res.append(-maxHeap[0][0])
        return res


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        https://algo.monster/problems/sliding_window_maximum
        """
        q = deque()  # stores *indices*
        res = []
        for i, cur in enumerate(nums):
            # Прежде чем поместить элемент в двухстороннюю очередь, мы сначала извлекаем из ее хвоста все те индексы,
            # значения которых меньше текущего значения.
            while q and nums[q[-1]] <= cur:
                q.pop()

            # Добавляем индекс текущего элемента в хвост очереди
            q.append(i)

            # Удаляем первый элемент очереди, если он находится за пределами окна
            if q[0] == i - k:
                q.popleft()

            # После k - 1 итераций начинаем добавлять первый элемент очереди в результирующий массив
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
