from typing import List


def test_1():
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    assert Solution().numOfSubarrays(arr, k, threshold) == 3


def test_2():
    arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
    k = 3
    threshold = 5
    assert Solution().numOfSubarrays(arr, k, threshold) == 6


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, right, res = 0, 0, 0
        prefix_sum = 0
        while right < len(arr):
            prefix_sum += arr[right]
            if right - left == k - 1:
                average = prefix_sum / k
                if average >= threshold:
                    res += 1

                left += 1

                prefix_sum -= arr[right - k + 1]

            right += 1

        return res
