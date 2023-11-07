import heapq


class SeatManager:

    def __init__(self, n: int):
        self.data = list(range(1, n + 1))
        heapq.heapify(self.data)

    def reserve(self) -> int:
        return heapq.heappop(self.data)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.data, seatNumber)
