from typing import Optional, List, Hashable, Set


class Node:
    """
    Graph node
    """

    def __init__(self, data: int, children: Optional[List['Node']] = None):
        self.data = data
        self.children = children

    def __repr__(self):
        return str(self.data)

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other):
        return self.data == other.data


def dfs_1(current: Node, target: int, visited: Set[Node]) -> Optional[Node]:
    """
    Обход графа в глубину с поиском значения атрибута Node.data
    :param current: Начальная вершина графа.
    :param target: искомое значение
    :param visited: посещенные вершины
    :return: node - найденная вершина. Если не найдено, None
    """
    if current.data == target:
        return current

    if current.children:
        for child in current.children:
            if child not in visited:
                visited.add(child)
                node = dfs_1(child, target, visited)
                if node:
                    return node

    return None  # вершина не найдена


def dfs(root: Node, target: int) -> Optional[Node]:
    """
    Обход графа в глубину с поиском значения атрибута Node.data
    :param root: Начальная вершина графа.
    :param target: искомое значение
    :return: node - найденная вершина. Если не найдено, None
    """
    visited = set()  # посещенные вершины
    stack = [root]
    while len(stack) > 0:  # пока стек не пуст
        current = stack.pop()

        if current.data == target:
            return current

        if current.children:
            for child in current.children:
                if child not in visited:
                    visited.add(child)
                    stack.append(child)

    return None  # вершина не найдена


def test_dfs():
    graph = Node(1, [
        Node(2, [Node(17)]),
        Node(3, [
            Node(5, [Node(7)]),
            Node(9),
        ]),
        Node(4, [Node(6)]),
    ])
    print('\n')

    # print(isinstance(Node(6), Hashable))

    # print(hash(Node(6)))

    node = dfs(graph, 6)
    assert node.data == 6

    node = dfs(graph, 7)
    assert node.data == 7

    node = dfs(graph, 7222)
    assert node is None
