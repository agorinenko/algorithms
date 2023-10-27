from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return eval_node(root)


def eval_node(node: Optional[TreeNode]) -> bool:
    if not node.left or not node.right:
        return node.val == 1

    r1 = eval_node(node.left)
    r2 = eval_node(node.right)
    if node.val == 2:
        return r1 or r2

    return r1 and r2
