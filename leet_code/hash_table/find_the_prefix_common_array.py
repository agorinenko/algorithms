from typing import List


def test_1():
    a = "sayhelloworld".split("hello")
    assert [0, 2, 3, 4] == Solution().findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4])


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        meta = {}
        ans = []
        c = 0
        for i in range(len(B)):
            a = A[i]
            b = B[i]

            if a not in meta:
                meta[a] = 0
            meta[a] += 1

            if meta[a] == 2:
                c += 1

            if b not in meta:
                meta[b] = 0
            meta[b] += 1


            if meta[b] == 2:
                c += 1
            # c = 0
            # for n in A[:i + 1]:
            #     if meta[n] == 2:
            #         c += 1

            ans.append(c)

        return ans
