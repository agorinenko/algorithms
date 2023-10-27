import sys


# def test_1():
#     assert main('ab', 'aabbccd') == 4


def main(j: str, s: str) -> int:
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
