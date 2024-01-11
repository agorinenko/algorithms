import collections


def test_1():
    assert Solution().countGoodSubstrings("aababcabc") == 4


def test_2():
    assert Solution().countGoodSubstrings("aaabbb") == 0


def test_3():
    assert Solution().countGoodSubstrings("xyzzaz") == 1


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left, right = 0, 0
        result = 0
        memory = collections.defaultdict(int)
        while right < len(s):
            right_char = s[right]
            memory[right_char] += 1

            if right - left == 3:
                left_char = s[left]
                memory[left_char] -= 1

                if memory[left_char] <= 0:
                    del memory[left_char]

                left += 1

            if len(memory) == 3:
                result += 1

            right += 1

        return result

    def countGoodSubstrings2(self, s: str) -> int:
        left, right = 0, 3
        result = 0
        while right <= len(s):
            sub_str = s[left:right]
            if len(sub_str) == len(set(sub_str)):
                result += 1

            right += 1
            left += 1

        return result
