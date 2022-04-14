"""
Problem: https://leetcode.com/problems/search-in-a-binary-search-tree/
Topics: Tree, Binary Search Tree, Binary Tree
Difficulty: Easy
Youtube Explanation: https://youtu.be/lbE6M5Ue99A
"""
class Solution:
    def searchBST(self, root, val):
        if not root:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def searchBSTSol2(self, root, val):
        current = root
        while current:
            if current.val == val:
                return current
            if val < current.val:
                current = current.left
            else:
                current = current.right
        return current
