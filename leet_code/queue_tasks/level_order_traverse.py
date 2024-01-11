# Definition for a binary tree node.
from collections import deque
from typing import Optional, List, Callable


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_main_1():
    graph = TreeNode(val=3,
                     left=TreeNode(val=9),
                     right=TreeNode(val=20,
                                    left=TreeNode(val=15),
                                    right=TreeNode(val=7)))
    assert [[3], [9, 20], [15, 7]] == Solution().levelOrder(graph)


def test_main_2():
    graph = TreeNode(val=1,
                     right=TreeNode(val=2))
    assert [[1],[2]] == Solution().levelOrder(graph)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        step_holder = {}

        def job(step, current_node):
            if step in step_holder:
                step_holder[step].append(current_node.val)
            else:
                step_holder[step] = [current_node.val]

        bfs(root, job)

        return list(step_holder.values())


def bfs(root: TreeNode, node_function: Callable):
    queue = deque()  # хранение всех вершин, которые ожидают обработки
    visited = set()  # вершины, которые уже посетили
    step = 0  # количество необходимых шагов, чтобы достичь искомую вершину
    # инициализация
    queue.append(root)
    visited.add(root)
    while len(queue) > 0:  # пока очередь не пуста
        size = len(queue)
        # обработка элементов, которые находятся в очереди, те вершин одного уровня
        for _ in range(size):
            current_node = queue.popleft()
            if not current_node:
                continue
            node_function(step, current_node)
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
        step += 1
