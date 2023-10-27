from collections import deque
from typing import Optional

from utils.tree import TreeNode, draw_tree, deserialize, tree_str_to_list, serialize


def test_1():
    root = deserialize([4, 2, 7, 1, 3, 6, 9])
    result = Solution().invertTree(root)
    assert serialize(result) == [4, 7, 2, 9, 6, 3, 1]


def test_2():
    root = deserialize([2, 1, 3])
    result = Solution().invertTree(root)
    assert serialize(result) == [2, 3, 1]


def test_3():
    root = deserialize([])
    result = Solution().invertTree(root)
    assert serialize(result) == []


def test_4():
    root = deserialize([1, 2])
    result = Solution().invertTree(root)
    assert serialize(result) == [1, None, 2]


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        levels_matrix = [deque([root])]
        while queue:
            level_size = len(queue)
            level_deque = deque()
            for _ in range(level_size):
                cur = queue.popleft()

                # level_deque.appendleft(cur.val if cur else None)

                level_deque.append(cur.left.val if cur.left else None)
                level_deque.append(cur.right.val if cur.right else None)

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

            levels_matrix.append(level_deque)
        levels_matrix.pop()
        # Second traverse
        queue = deque([root])
        step = 0
        while queue:
            level_size = len(queue)

            for i in range(level_size):
                cur = queue.popleft()
                cur.val = levels_matrix[step].popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            step += 1

        return root
