# Definition for a binary tree node.
from typing import List, Optional


def test_1():
    assert Solution().bstFromPreorder([8, 5, 1, 7, 10, 12]) == TreeNode(val=8)


def test_2():
    assert Solution().bstFromPreorder([4, 2]) == TreeNode(val=4)


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
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return build_node(preorder)


def build_node(preorder: List[int]) -> Optional[TreeNode]:
    if not preorder:
        return None

    root_val = preorder[0]
    root = TreeNode(val=root_val)
    if len(preorder) == 1:
        return root

    idx = len(preorder)
    for i in range(1, len(preorder)):
        val = preorder[i]
        if val > root_val:
            idx = i
            break
    left_preorder = preorder[1:idx]
    right_preorder = preorder[idx:]
    root.left = build_sub_tree(left_preorder)
    root.right = build_sub_tree(right_preorder)
    return root


def build_sub_tree(preorder: List[int]) -> Optional[TreeNode]:
    return build_node(preorder)
