# Definition for a binary tree node.
import math
from typing import Optional


def test_1():
    root = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)), right=TreeNode(val=6))
    assert Solution().getMinimumDifference(root) == 1


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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        ans = math.inf
        prev = None
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if prev is not None:
                i = current.val - prev
                if i < ans:
                    ans = i

            prev = current.val
            # ans.append(current.val)

            current = current.right

        return ans
