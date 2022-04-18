"""
Problem: https://leetcode.com/problems/increasing-order-search-tree/
Topics: Binary Search Tree, Tree, Binary Tree, Depth first Search
Difficulty: Easy
Youtube Explanation: https://youtu.be/TlKNW3D8GNg
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root):

        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        def construct(values, i):
            if i == len(values):
                return None

            node = TreeNode(values[i])
            node.right = construct(values, i + 1)
            return node

        values = inorder(root)
        return construct(values, 0)

    def increasingBSTSol2(self, root):

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            self.current.right = TreeNode(node.val)
            self.current = self.current.right

            inorder(node.right)

        sentinel = TreeNode(-1)
        self.current = sentinel
        inorder(root)
        return sentinel.right
