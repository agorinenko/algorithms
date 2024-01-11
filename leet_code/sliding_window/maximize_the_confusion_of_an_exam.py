def test_1():
    assert Solution().maxConsecutiveAnswers("TTFF", 2) == 4


def test_2():
    assert Solution().maxConsecutiveAnswers("TFFT", 1) == 3


def test_3():
    assert Solution().maxConsecutiveAnswers("TTFTTFTT", 1) == 5


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        if len(answerKey) == 0:
            return 0
        if len(answerKey) == 1:
            return 1

        left, right, res = 0, 0, 0
        _k = k

        while right < len(answerKey):
            cur_char = answerKey[right]

            if cur_char == 'F':
                k -= 1

            if k < 0:
                res = max(res, right - left)
                left_char = answerKey[left]
                k = _k
                while left_char == 'F':
                    left += 1
                    left_char = answerKey[left]

            right += 1

        return res if res > 0 else right-left
