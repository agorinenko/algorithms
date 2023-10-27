from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root1:
            return root2

        if not root2:
            return root1

        ans = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
        ans.left = self.mergeTrees(root1.left, root2.left)
        ans.right = self.mergeTrees(root1.right, root2.right)

        return ans

    def mergeTrees2(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2

        stack = [(root1, root2)]

        while stack:
            curr = stack.pop()
            if not curr[0] or not curr[1]:
                continue

            curr[0].val += curr[1].val

            if not curr[0].left:
                curr[0].left = curr[1].left
            else:
                stack.append((curr[0].left, curr[1].left))

            if not curr[0].right:
                curr[0].right = curr[1].right
            else:
                stack.append((curr[0].right, curr[1].right))

        return root1
