# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        ordered_nodes = []
        in_order(root, ordered_nodes)
        for i in range(len(ordered_nodes) - 1):
            node = ordered_nodes[i]
            next_node = ordered_nodes[i + 1]
            node.left = None
            node.right = next_node

        last_node = ordered_nodes[len(ordered_nodes) - 1]
        last_node.left = None
        last_node.right = None

        return ordered_nodes[0]


def in_order(node: TreeNode, ordered_nodes: list[TreeNode]):
    if node:
        in_order(node.left, ordered_nodes)
        ordered_nodes.append(node)
        in_order(node.right, ordered_nodes)
