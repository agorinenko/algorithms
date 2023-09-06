from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return is_symmetric(root.left, root.right)


def is_symmetric(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    if not left and not right:
        return True

    if not left or not right:
        return False

    left_symmetric = is_symmetric(left.left, right.right)
    right_symmetric = is_symmetric(left.right, right.left)

    return left.val == right.val and left_symmetric and right_symmetric
