from typing import List, Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        traverse_node(res, root)

        return res


def traverse_node(res: List[int], node: Optional[Node]) -> None:
    if not node:
        return None

    if node.children:
        for child in node.children:
            traverse_node(res, child)

    res.append(node.val)
