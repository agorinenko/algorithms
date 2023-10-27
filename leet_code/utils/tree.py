import turtle
from collections import deque
from typing import List


class TreeNode:
    """ Node """

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


def tree_str_to_list(tree_str: str) -> List[int]:
    if not tree_str:
        return []
    tree_str = tree_str.strip('[]{}')
    if not tree_str:
        return []

    return [None if val == 'null' else int(val) for val in tree_str.split(',')]


def serialize(root: TreeNode) -> List[int]:
    queue = deque([root])
    array = [root.val]
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            cur = queue.popleft()

            array.append(cur.left.val if cur.left else None)
            array.append(cur.right.val if cur.right else None)

            if cur.left:
                queue.append(cur.left)

            if cur.right:
                queue.append(cur.right)

    for _ in range(len(array)):
        if array[-1] is None:
            array.pop()
    return array


def deserialize(array: List[int]):
    """ Deserialize tree """
    if not array:
        return None

    nodes = [None if val is None else TreeNode(val=int(val)) for val in array]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


def draw_tree(root: TreeNode):
    def height(node):
        return 1 + max(height(node.left), height(node.right)) if node else -1

    def jump_to(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jump_to(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jump_to(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jump_to(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


def test_1():
    # draw_tree(deserialize(tree_str_to_list('[1,2,3,null,null,4,null,null,5]')))
    draw_tree(deserialize(tree_str_to_list('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')))


def test_2():
    arr = [1, 2, 3, None, None, 4, None, None, 5]
    root = deserialize(arr)
    assert serialize(root) == arr


def test_3():
    arr = [2, 1, 3, 0, 7, 9, 1, 2, None, 1, 0, None, None, 8, 8, None, None, None, None, 7]
    root = deserialize(arr)
    assert serialize(root) == arr
