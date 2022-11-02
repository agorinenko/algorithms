from leet_code.hash_table.find_duplicate_subtrees import Solution, TreeNode


def test_main_1():
    root = TreeNode(1,
                    left=TreeNode(2, left=TreeNode(4)),
                    right=TreeNode(3, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(4)))
    s = Solution()
    assert s.find_duplicate_subtrees(root) == [[2, 4], [4]]
