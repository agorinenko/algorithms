# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def search_bst(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Поиск ключа в бинарном дереве
    :param node: узле
    :param val: искомое значение
    :return: найденный узел, None если не найдено
    """
    if not node:
        return None

    if node.val == val:
        return node

    if node.val > val:
        return search_bst(node.left, val)

    if node.val < val:
        return search_bst(node.right, val)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return search_bst(root, val)


def test_1():
    graph = TreeNode(val=4,
                     left=TreeNode(val=2,
                                   left=TreeNode(val=1),
                                   right=TreeNode(val=3)),
                     right=TreeNode(val=7))
    assert 2 == Solution().searchBST(graph, 2).val
