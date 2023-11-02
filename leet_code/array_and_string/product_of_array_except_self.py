from typing import List


def test_1():
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_2():
    assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_3():
    assert Solution().productExceptSelf([1, 0]) == [0, 1]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        ptr = 1
        for i in range(len(nums)):
            res[i] *= ptr
            ptr *= nums[i]

        ptr = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= ptr
            ptr *= nums[i]

        return res

    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        prefix_array = [1] * len(nums)
        for i in range(1, len(nums)):
            # Движемся с лева на право ->
            # Для позиции i значение равно произведению предыдущего элемента и кумулятивного произведения элементов,
            # идущих до предыдущего
            prefix_array[i] = nums[i - 1] * prefix_array[i - 1]

        suffix_array = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            # Движемся с права на лево <-
            # Для позиции i значение равно произведению следующего элемента и кумулятивного произведения элементов,
            # идущих после следующего
            suffix_array[i] = nums[i + 1] * suffix_array[i + 1]

        res = [0] * len(nums)

        for i in range(0, len(nums)):
            # prefix_array[i] * suffix_array[i] - это произведение кумулятивных произведений до индекса i и после него
            res[i] = prefix_array[i] * suffix_array[i]

        return res
