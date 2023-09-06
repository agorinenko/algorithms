from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        node = root
        while (root):
            child_head = None  # move to the next level
            child = None
            while (root):
                if root.left:
                    if child_head is None:
                        child_head = root.left
                        child = root.left
                    else:
                        child.next = root.left
                        child = child.next

                if root.right:
                    if child_head is None:
                        child_head = root.right
                        child = root.right
                    else:
                        child.next = root.right
                        child = child.next

                root = root.next

            # Next level
            root = child_head
        return node


def bfs(root: Node):
    if not root:
        return

    queue = deque()
    visited = set()

    queue.append(root)
    visited.add(root)

    while len(queue) > 0:
        row_nodes = []

        size = len(queue)
        for _ in range(size):
            current_node = queue.popleft()

            row_nodes.append(current_node)
            children = []

            if current_node.left:
                children.append(current_node.left)

            if current_node.right:
                children.append(current_node.right)

            if children:
                for child in children:
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)

        for i in range(len(row_nodes) - 1):
            row_nodes[i].next = row_nodes[i + 1]
