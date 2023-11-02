class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = bin(n)
        a = n >> 1
        c = 0
        for i in bin_str:
            if i == '1':
                c += 1

        return c

def test_1():
    Solution().hammingWeight(2)