def test_1():
    assert Solution().kthGrammar(1, 1) == 0


def test_2():
    assert Solution().kthGrammar(2, 1) == 0


def test_3():
    assert Solution().kthGrammar(2, 2) == 1


def test_4():
    assert Solution().kthGrammar(5, 5) == 1


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def depth_first_search(n: int, k: int, root_val: int) -> int:
            if n == 1:
                return root_val

            total_nodes_count = 2 ** (n - 1)

            # Целевая вершина находится в правом поддереве текущего узла
            if k > (total_nodes_count / 2):
                next_root_val = 1 if root_val == 0 else 0
                return depth_first_search(n - 1, k - (total_nodes_count / 2), next_root_val)
            # Напротив, целевая вершина находится в левом поддереве текущего узла
            else:
                next_root_val = 0 if root_val == 0 else 1
                return depth_first_search(n - 1, k, next_root_val)

        return depth_first_search(n, k, 0)


