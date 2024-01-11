def test_1():
    s = "abcabcbb"
    assert Solution().lengthOfLongestSubstring(s) == 3


def test_2():
    s = "pwwkew"
    assert Solution().lengthOfLongestSubstring(s) == 3


def test_3():
    s = "bbbbb"
    assert Solution().lengthOfLongestSubstring(s) == 1


def test_4():
    s = " "
    assert Solution().lengthOfLongestSubstring(s) == 1


def test_5():
    s = "au"
    assert Solution().lengthOfLongestSubstring(s) == 2


def test_6():
    s = "aab"
    assert Solution().lengthOfLongestSubstring(s) == 2


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1) Определяем левую и правую границу. Размер окна может быть фиксированного размера или динамическим
        # (зависит от какого-то условия)
        left = 0
        max_len = 0
        uniq = set()
        # 2) Двигаем правый указатель
        for right, cur_char in enumerate(s):
            # 3) Проводим необходимые проверки, например уникальны ли все символы в окне, соответствует ли размер окна
            # заданным критериям. Обычно проверки основываются на каком-то состоянии
            while cur_char in uniq:
                left_char = s[left]
                uniq.remove(left_char)
                # Если надо, передвигаем левый указатель
                left += 1

            uniq.add(cur_char)
            # Проверяем результат
            max_len = max(right - left + 1, max_len)

        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l = 0
        max_len = 0
        while l < len(s):
            uniq = {s[l]}

            for r in range(l + 1, len(s)):
                if s[r] not in uniq:
                    uniq.add(s[r])
                else:
                    break

            uniq_len = len(uniq)
            max_len = max(max_len, uniq_len)

            l += 1

        return max_len
