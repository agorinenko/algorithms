import sys
from typing import List


def test_1():
    assert main([1, 1, 1, 1, 0, 1, 1]) == 4


def test_2():
    assert main([1, 1, 0, 1, 1, 1, 1]) == 4


def main(bin_array: List[int]) -> int:
    s_metrics = dict.fromkeys(s, 0)
    for c in s:
        s_metrics[c] += 1

    res = 0
    for c in j:
        res += s_metrics.get(c, 0)

    return res


# if __name__ == '__main__':
j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

print(main(j, s))
