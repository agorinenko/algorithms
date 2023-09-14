# Definition for a binary tree node.
from typing import List, Optional


def test_1():
    assert Solution().sortedArrayToBST([-10, -3, 0, 5, 9]) == TreeNode(val=0)


def test_2():
    assert Solution().sortedArrayToBST([1, 3]) == TreeNode(val=3)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

    def __hash__(self):
        return hash(self.val)

    def __eq__(self, other):
        return self.val == other.val


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)

        if not total_nums:
            return None

        middle = total_nums // 2
        root = TreeNode(val=nums[middle],
                        left=self.sortedArrayToBST(nums[:middle]),
                        right=self.sortedArrayToBST(nums[middle+1:]))

        return root
