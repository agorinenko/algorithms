from typing import List


def test_1():
    assert Solution().fizzBuzz(3) == ["1", "2", "Fizz"]


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = [str(i) for i in range(1, n + 1)]
        for i in range(len(arr)):
            j = i + 1
            if j % 3 == 0 and j % 5 == 0:
                arr[i] = "FizzBuzz"
            elif j % 3 == 0:
                arr[i] = "Fizz"
            elif j % 5 == 0:
                arr[i] = "Buzz"
        return arr
