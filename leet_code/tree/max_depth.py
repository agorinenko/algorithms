from typing import Optional, Callable


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_main_1():
    graph = TreeNode(val=3,
                     left=TreeNode(val=9),
                     right=TreeNode(val=20,
                                    left=TreeNode(val=15),
                                    right=TreeNode(val=7)))
    assert 3 == Solution().maxDepth(graph)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result_depth = []

        def callback(depth):
            result_depth.append(depth)

        max_depth(callback, root)
        if not result_depth:
            return 0

        return max(result_depth)


def max_depth(callback: Callable, root: Optional[TreeNode], depth: Optional[int] = 1):
    if not root:
        return None

    if not root.left and not root.right:
        callback(depth)

    max_depth(callback, root.left, depth + 1)
    max_depth(callback, root.right, depth + 1)
