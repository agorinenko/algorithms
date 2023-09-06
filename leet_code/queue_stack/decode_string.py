from typing import Tuple, Optional, Callable, Any


def test_main_1():
    assert Solution().decodeString('3[a2[c]]') == 'accaccacc'

class Solution:
    def decodeString(self, s: str) -> str:
        return decode_string(s)


def decode_string(s: str) -> str:
    s_list = []
    for c in s:
        status, i = try_parse_int(c)
        if status:
            pass
        else:
            s_list.append(c)
    return ''.join(s_list)


def try_parse_int(i: str) -> Tuple[bool, Optional[int]]:
    """
    Parse object to int
    :param i: object
    :return: status, int object
    """
    return _try_parse(i, int)

def _try_parse(i: str, to_type: Callable, *args, except_errors: Optional[Tuple] = None) -> Tuple[bool, Optional[Any]]:
    except_errors = except_errors or (ValueError,)
    try:
        return True, to_type(i, *args)
    except except_errors:
        return False, None