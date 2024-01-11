# Definition for a binary tree node.
from collections import deque
from typing import Optional, List, Callable


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        inorder_recursive_dfs(lambda x: result.append(x.val), root)

        return result


def test_inorder_recursive_dfs():
    print('\n')

    graph = TreeNode(val=17,
                     left=TreeNode(val=2, left=TreeNode(val=7)),
                     right=TreeNode(val=9,
                                    left=TreeNode(val=1, right=TreeNode(val=10)),
                                    right=TreeNode(val=5)))

    inorder_recursive_dfs(lambda x: print(x), graph)


def test_inorder_dfs():
    print('\n')

    graph = TreeNode(val='F',
                     left=TreeNode(val='B',
                                   left=TreeNode(val='A'),
                                   right=TreeNode(val='D',
                                                  left=TreeNode(val='C'),
                                                  right=TreeNode(val='E'))),
                     right=TreeNode(val='G',
                                    right=TreeNode(val='I', left=TreeNode(val='H'))))

    list_1 = []
    list_2 = []
    inorder_stack_dfs(lambda x: list_1.append(x.val), graph)
    inorder_recursive_dfs(lambda x: list_2.append(x.val), graph)

    assert list_1 == list_2


def test_preorder_dfs():
    print('\n')

    graph = TreeNode(val='F',
                     left=TreeNode(val='B',
                                   left=TreeNode(val='A'),
                                   right=TreeNode(val='D',
                                                  left=TreeNode(val='C'),
                                                  right=TreeNode(val='E'))),
                     right=TreeNode(val='G',
                                    right=TreeNode(val='I', left=TreeNode(val='H'))))

    list_1 = []
    list_2 = []
    preorder_stack_dfs(lambda x: list_1.append(x.val), graph)
    preorder_recursive_dfs(lambda x: list_2.append(x.val), graph)

    assert list_1 == list_2


def test_postorder_dfs():
    print('\n')

    graph = TreeNode(val='F',
                     left=TreeNode(val='B',
                                   left=TreeNode(val='A'),
                                   right=TreeNode(val='D',
                                                  left=TreeNode(val='C'),
                                                  right=TreeNode(val='E'))),
                     right=TreeNode(val='G',
                                    right=TreeNode(val='I', left=TreeNode(val='H'))))

    list_1 = []
    list_2 = []
    postorder_stack_dfs(lambda x: list_1.append(x.val), graph)
    postorder_recursive_dfs(lambda x: list_2.append(x.val), graph)

    assert list_1 == list_2


def inorder_recursive_dfs(node_function: Callable, node: Optional[TreeNode] = None):
    if node:
        inorder_recursive_dfs(node_function, node.left)
        node_function(node)
        inorder_recursive_dfs(node_function, node.right)


def inorder_stack_dfs(node_function: Callable, node: Optional[TreeNode] = None):
    stack = []
    current = node
    while current or len(stack) > 0:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        node_function(current)

        current = current.right


def postorder_recursive_dfs(node_function: Callable, node: Optional[TreeNode] = None):
    if node:
        postorder_recursive_dfs(node_function, node.left)
        postorder_recursive_dfs(node_function, node.right)

        node_function(node)


def postorder_stack_dfs(node_function: Callable, node: Optional[TreeNode] = None):
    stack = []
    last_node_visited = None
    while node or len(stack) > 0:
        if node:
            stack.append(node)
            node = node.left
        else:
            peek_node = stack[-1]
            if peek_node.right and last_node_visited != peek_node.right:
                node = peek_node.right
            else:
                node_function(peek_node)
                last_node_visited = stack.pop()


    # stack = [node]
    # out = []
    # while len(stack) > 0:
    #     current = stack.pop()
    #     out.append(current)
    #
    #     if current.left:
    #         stack.append(current.left)
    #
    #     if current.right:
    #         stack.append(current.right)
    #
    # while out:
    #     node_function(out.pop())



def preorder_recursive_dfs(node_function: Callable, node: Optional[TreeNode] = None):
    if node:
        node_function(node)

        preorder_recursive_dfs(node_function, node.left)
        preorder_recursive_dfs(node_function, node.right)


def preorder_stack_dfs(node_function: Callable, node: Optional[TreeNode] = None):
    stack = [node]

    while stack:
        node = stack.pop()
        if node:
            node_function(node)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
