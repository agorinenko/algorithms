"""
# Definition for a Node.
"""
from typing import Dict, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return str(self.val)


def build_graph() -> Node:
    """
    Given Graph:
    1--2
    | |
    4--3
    """
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node3, node1]

    return node1


def test_main_1():
    node = build_graph()
    clone = Solution().cloneGraph(node)
    assert clone


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return dfs(node, {})


def dfs(current: Node, visited: Dict) -> Optional[Node]:
    """
    Обход графа в глубину
    """
    if current is None:
        return None

    new_node = Node(val=current.val)
    visited[current.val] = new_node

    if current.neighbors:
        for child in current.neighbors:
            if child.val not in visited:
                new_child = dfs(child, visited)
                new_node.neighbors.append(new_child)
            else:
                new_node.neighbors.append(visited[child.val])

    return new_node
