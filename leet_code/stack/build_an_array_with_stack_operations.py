from typing import List


def test_1():
    assert Solution().buildArray([1, 3], 3) == ["Push", "Push", "Pop", "Push"]


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        stack = []
        target_set = set(target)
        for num in range(1, n + 1):
            if len(stack) == len(target):
                break
            if num in target_set:
                result.append('Push')
                stack.append(num)
            else:
                result.append('Push')
                stack.append(num)
                result.append('Pop')
                stack.pop()

        return result
