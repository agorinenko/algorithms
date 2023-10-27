# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack_a = [original]
        stack_b = [cloned]
        while stack_a:
            cur = stack_a.pop()
            cur_b = stack_b.pop()
            if cur is target:
                return cur_b

            if cur.right:
                stack_a.append(cur.right)
                stack_b.append(cur_b.right)

            if cur.left:
                stack_a.append(cur.left)
                stack_b.append(cur_b.left)

        return None


