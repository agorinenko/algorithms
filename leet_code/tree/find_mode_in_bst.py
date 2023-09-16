from collections import deque
from typing import List, Optional


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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """in-order"""
        extra_space = {}
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if current.val in extra_space:
                extra_space[current.val] += 1
            else:
                extra_space[current.val] = 1

            current = current.right

        max_count = max(extra_space.values())
        return [i for i, c in extra_space.items() if c == max_count]

class Solution2:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        extra_space = {}
        stack = [root]

        while stack:
            node = stack.pop()
            if node.val in extra_space:
                extra_space[node.val] += 1
            else:
                extra_space[node.val] = 1

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        max_count = max(extra_space.values())
        return [i for i, c in extra_space.items() if c == max_count]

class Solution1:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        extra_space = {}
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.val in extra_space:
                    extra_space[node.val] += 1
                else:
                    extra_space[node.val] = 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        max_count = max(extra_space.values())
        return [i for i, c in extra_space.items() if c == max_count]
