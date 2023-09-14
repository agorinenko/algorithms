from typing import Callable, Optional


def test_1():
    root = TreeNode(val=4,
                    left=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=2, right=TreeNode(val=3))),
                    right=TreeNode(val=6, left=TreeNode(val=5), right=TreeNode(val=7, right=TreeNode(val=8))))

    Solution().bstToGst(root)
    assert root.val == 30


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def __init__(self):
        self.val = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.inorder_recursive_dfs(self.set_val, root)

        return root


    def set_val(self, node: TreeNode):
        node.val += self.val
        self.val = node.val


    def inorder_recursive_dfs(self, node_function: Callable, node: Optional[TreeNode] = None):
        stack = []
        current = node
        while current or len(stack) > 0:
            while current:
                stack.append(current)
                current = current.right

            current = stack.pop()
            node_function(current)

            current = current.left
