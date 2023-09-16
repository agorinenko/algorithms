from collections import deque
from typing import Optional


def test_1():
    root = TreeNode(val=2, right=TreeNode(val=3))
    assert not Solution().findTarget(root, k=6)


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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = deque()
        queue.append(root)
        nums = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                target = queue.popleft()

                i = k - target.val
                if i in nums:
                    return True

                nums.add(target.val)

                if target.left:
                    queue.append(target.left)

                if target.right:
                    queue.append(target.right)

        return False
