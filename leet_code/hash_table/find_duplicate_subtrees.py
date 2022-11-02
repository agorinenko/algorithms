"""
https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1127/
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '#'.join([str(self.val), str(self.left), str(self.right)])


class Solution:
    def find_duplicate_subtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        data = {}

        def serialization(node, path):
            if node is None: return '#'

            path = ','.join([str(node.val), serialization(node.left, path), serialization(node.right, path)])

            if path in data:
                data[path] += 1
                if data[path] == 2:
                    res.append(node)
            else:
                data[path] = 1

            return path

        serialization(root, '')

        return res
