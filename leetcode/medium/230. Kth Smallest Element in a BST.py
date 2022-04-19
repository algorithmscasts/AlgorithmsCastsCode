"""
Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Topics: Binary Search Tree, Tree, Binary Tree, Depth first Search
Difficulty: Medium
Youtube Explanation: https://youtu.be/W2GxbbBTPqo
"""


class Solution:
    def kthSmallest(self, root, k):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        values = inorder(root)
        return values[k - 1]

    def kthSmallestSol2(self, root, k):
        def inorder(node):
            if not node:
                return []
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.kth = node.val
            else:
                inorder(node.right)

        self.count = 0
        self.kth = None
        inorder(root)
        return self.kth

    def kthSmallestSol3(self, root, k):
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
