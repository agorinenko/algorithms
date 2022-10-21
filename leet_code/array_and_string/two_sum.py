from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        num_set = set(numbers)
        for idx in range(len(numbers)):
            f = numbers[idx]
            s = target - f
            if s in num_set:
                for idx2 in range(idx + 1, len(numbers)):
                    if s == numbers[idx2]:
                        return [idx + 1, idx2 + 1]

        return []

    def two_sum_slow(self, numbers: List[int], target: int) -> List[int]:
        for idx in range(len(numbers)):
            for idx2 in range(idx + 1, len(numbers)):
                if numbers[idx] + numbers[idx2] == target:
                    return [idx+1, idx2+1]

        return []
