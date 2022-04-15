"""
Problem: https://leetcode.com/problems/trim-a-binary-search-tree/
Topics: Binary Search Tree, Tree, Depth first Search
Difficulty: Medium
Youtube Explanation: https://youtu.be/eCMpgYNHNos
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root, low, high):
        def preorder_bounds(node):
            if not node:
                return

            if node.val in range(low, high + 1):
                self.preorder.append(node.val)

            if node.val >= low:
                preorder_bounds(node.left)
            if node.val <= high:
                preorder_bounds(node.right)

        def reconstruct(inorder, limit):
            if self.i >= len(inorder) or inorder[self.i] > limit:
                return None

            node = TreeNode(inorder[self.i])

            self.i += 1

            node.left = reconstruct(inorder, node.val)
            node.right = reconstruct(inorder, limit)
            return node

        self.preorder = []
        preorder_bounds(root)

        self.i = 0
        node = reconstruct(self.preorder, float('inf'))
        return node

    def trimBSTSol2(self, root, low, high):
        def helper(node):
            if not node:
                return None

            if node.val < low:
                return helper(node.right)

            if node.val > high:
                return helper(node.left)

            node.left = helper(node.left)
            node.right = helper(node.right)
            return node

        return helper(root)
