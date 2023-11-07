from typing import Tuple, Optional, Callable, Any


def test_main_1():
    assert Solution().decodeString('3[a2[c]]') == 'accaccacc'


def test_main_2():
    assert Solution().decodeString('xx3[a2[c]]') == 'xxaccaccacc'


def test_main_3():
    assert Solution().decodeString("3[a]2[bc]") == 'aaabcbc'


def test_main_4():
    assert Solution().decodeString('100[a]') == 'a' * 100

def test_main_5():
    assert Solution().decodeString('abc') == 'abc'

def test_main_6():
    assert Solution().decodeString('1[1[1[]]]') == ''

class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        num_stack = []
        sub_str = ''
        ptr = 0
        # 1) Iterate by string
        while ptr < len(s):
            c = s[ptr]
            if c.isnumeric():
                # 2) If char is number, calculate full number in string
                count = c
                ptr += 1
                while s[ptr].isnumeric():
                    count += s[ptr]
                    ptr += 1
                # 3) Add int value in to stack of numbers
                num_stack.append(int(count))
            elif c == '[':
                # 4) If char is '[', append sub string to stack of strings and clear sub string
                str_stack.append(sub_str)
                sub_str = ''
                ptr += 1
            elif c == ']':
                # 5) If char is ']', pop string from stack of strings, pop number from stack of numbers and multiply them
                i = [str_stack.pop()]
                count = num_stack.pop()
                for _ in range(count):
                    i.append(sub_str)
                sub_str = ''.join(i)
                ptr += 1
            else:
                # 6) Add char to substring.
                sub_str += c
                ptr += 1
        # 7) Return substring
        return sub_str


def decode_string(s: str) -> str:
    s_list = []
    start_ptr = 0
    while start_ptr < len(s):
        c = s[start_ptr]
        if c.isnumeric():
            count = c
            start_ptr += 1
            while s[start_ptr].isnumeric():
                count += s[start_ptr]
                start_ptr += 1

            sub_str = _get_substr(start_ptr, s)
            sub_str = decode_string(sub_str)
            s_list.append(sub_str * int(count))
            start_ptr += len(sub_str) + 2
        else:
            if not c == '[' and not c == ']':
                s_list.append(c)
            start_ptr += 1

    return ''.join(s_list)


def _get_substr(start_ptr: int, s: str) -> str:
    tmp = []
    res = []
    while start_ptr < len(s):
        if s[start_ptr] == '[':
            tmp.append('[')
        elif s[start_ptr] == ']':
            tmp.pop()

        res.append(s[start_ptr])

        if not tmp:
            res = ''.join(res)
            return res[1: len(res) - 1]

        start_ptr += 1

    raise ValueError(f'Invalid string "{s}".')
