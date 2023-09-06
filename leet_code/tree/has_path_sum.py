from typing import Optional, Callable


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def test_main_1():
    graph = TreeNode(val=5,
                     left=TreeNode(val=4,
                                   left=TreeNode(val=11,
                                                 left=TreeNode(val=7),
                                                 right=TreeNode(val=2))),
                     right=TreeNode(val=8,
                                    left=TreeNode(val=13),
                                    right=TreeNode(val=4, right=TreeNode(val=1))))

    assert Solution().hasPathSum(graph, 22)


def test_main_2():
    graph = TreeNode(val=3,
                     left=TreeNode(val=9),
                     right=TreeNode(val=20,
                                    left=TreeNode(val=15),
                                    right=TreeNode(val=7)))
    assert not Solution().hasPathSum(graph, 22)


def test_main_3():
    graph = TreeNode(val=1,
                     left=TreeNode(val=2),
                     )
    assert not Solution().hasPathSum(graph, 1)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        results = []

        def c(current_sum):
            results.append(targetSum == current_sum)

        has_path_sum(c, root, 0)

        return any(results)


def has_path_sum(callback: Callable, current_node: Optional[TreeNode], current_sum: int):
    if not current_node:
        return

    has_path_sum(callback, current_node.left, current_sum + current_node.val)
    has_path_sum(callback, current_node.right, current_sum + current_node.val)

    if not current_node.left and not current_node.right:
        callback(current_sum + current_node.val)
