import collections
from typing import List


def test_main_1():
    assert Solution().canVisitAllRooms([[1], [2], [3], []])


def test_main_2():
    assert not Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])


def test_main_3():
    assert Solution().canVisitAllRooms([[2], [], [1]])


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = collections.deque(rooms[0])
        room_visits = {0}
        while keys:
            room_idx = keys.popleft()
            if room_idx in room_visits:
                continue

            for key in rooms[room_idx]:
                keys.append(key)

            room_visits.add(room_idx)

        return len(room_visits) == len(rooms)
