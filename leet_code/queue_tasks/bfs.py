from collections import deque
from typing import Optional, List, Tuple, Hashable


class Node:
    def __init__(self, data: int, children: Optional[List['Node']] = None):
        self.data = data
        self.children = children

    def __repr__(self):
        return str(self.data)

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other):
        return self.data == other.data


def test_bfs():
    graph = Node(1, [
        Node(2, [Node(7)]),
        Node(3, [
            Node(5, [Node(7)]),
            Node(6),
        ]),
        Node(4, [Node(6)]),
    ])
    print('\n')

    print(isinstance(Node(6), Hashable))

    print(hash(Node(6)))

    step, node = bfs_2(graph, 6)
    assert 2 == step
    assert node.data == 6

    step, node = bfs_2(graph, 7)
    assert 2 == step
    assert node.data == 7


def bfs(root: Node, target: int) -> Tuple[int, Optional[Node]]:
    """
    Обход графа в ширину с поиском значения атрибута Node.data
    :param root: Начальная вершина графа.
    :param target: искомое значение
    :return: (step, node) - кратчайший путь между вершинами, найденная вершина. Если не найдено, None
    """
    queue = deque()  # хранение всех вершин, которые ожидают обработки
    step = 0  # количество необходимых шагов, чтобы достичь искомую вершину
    # инициализация
    queue.append(root)
    while len(queue) > 0:  # пока очередь не пуста
        print(f'============== Step: {step} ==============')
        size = len(queue)
        # обработка элементов, которые находятся в очереди, те вершин одного уровня
        for _ in range(size):
            current_node = queue.popleft()
            print(f'Node: {current_node}')
            if current_node.data == target:
                return step, current_node
            if current_node.children:
                for child in current_node.children:
                    queue.append(child)
        step += 1

    return step, None  # вершина не найдена


def bfs_2(root: Node, target: int) -> Tuple[int, Optional[Node]]:
    """
    Обход графа в ширину без посещения уже обработанных вершин с поиском значения атрибута Node.data
    :param root: Начальная вершина графа.
    :param target: искомое значение
    :return: (step, node) - кратчайший путь между вершинами, найденная вершина. Если не найдено, None
    """
    queue = deque()  # хранение всех вершин, которые ожидают обработки
    visited = set()  # вершины, которые уже посетили
    step = 0  # количество необходимых шагов, чтобы достичь искомую вершину
    # инициализация
    queue.append(root)
    visited.add(root)
    while len(queue) > 0:  # пока очередь не пуста
        print(f'============== Step: {step} ==============')
        size = len(queue)
        # обработка элементов, которые находятся в очереди, те вершин одного уровня
        for _ in range(size):
            current_node = queue.popleft()
            print(f'Node: {current_node}')
            if current_node.data == target:
                return step, current_node
            if current_node.children:
                for child in current_node.children:
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)
        step += 1

    return step, None  # вершина не найдена
