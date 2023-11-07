def test_1():
    assert Solution().isPalindrome('A man, a plan, a canal: Panama')


def test_2():
    assert not Solution().isPalindrome('race a car')


def test_3():
    assert Solution().isPalindrome(' ')


def test_4():
    assert Solution().isPalindrome('.,')


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr = 0
        right_ptr = len(s) - 1

        while left_ptr < right_ptr:
            while not s[left_ptr].isalnum() and left_ptr < right_ptr:
                left_ptr += 1

            while not s[right_ptr].isalnum() and left_ptr < right_ptr:
                right_ptr -= 1
            # В строке нет ни одной буквы-цифры и указатели встретились
            if left_ptr == right_ptr and not s[left_ptr].isalnum():
                return True

            if s[left_ptr].lower() != s[right_ptr].lower():
                return False

            left_ptr += 1
            right_ptr -= 1

        return True
