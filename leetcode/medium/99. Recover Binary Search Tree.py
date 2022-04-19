"""
Problem: https://leetcode.com/problems/recover-binary-search-tree/
Topics: Binary Search Tree, Tree, Binary Tree, Depth first Search
Difficulty: Medium
Youtube Explanation: https://youtu.be/cVm_jq5nJSw
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recoverTree(self, root):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node] + inorder(node.right)

        inorder_nodes = inorder(root)
        sorted_values = sorted([x.val for x in inorder_nodes])
        for i in range(len(sorted_values)):
            inorder_nodes[i].val = sorted_values[i]

    def recoverTreeSol2(self, root):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node] + inorder(node.right)

        inorder_nodes = inorder(root)
        # fist mistake is value at i - 1 when val at i - 1 >= val at i
        # second mistake val at i when val at i - 1 >= val at i
        first_mistake, second_mistake = -1, -1
        for i in range(1, len(inorder_nodes)):
            if inorder_nodes[i - 1].val >= inorder_nodes[i].val:
                if first_mistake == -1:
                    first_mistake = i - 1
                second_mistake = i  # we always set if for case when they are consecutif

        inorder_nodes[first_mistake].val, inorder_nodes[second_mistake].val = inorder_nodes[second_mistake].val, \
                                                                              inorder_nodes[first_mistake].val

    def recoverTreeSol3(self, root):

        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node] + inorder(node.right)

        inorder_nodes = inorder(root)
        first_mistake, second_mistake = None, None
        for i in range(1, len(inorder_nodes)):
            prev = inorder_nodes[i - 1]
            curr = inorder_nodes[i]
            if prev.val >= curr.val:
                if not first_mistake:
                    first_mistake = prev
                second_mistake = curr

        first_mistake.val, second_mistake.val = second_mistake.val, first_mistake.val

    def recoverTreeSol4(self, root):
        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev and self.prev.val >= node.val:
                if not self.first_mistake:
                    self.first_mistake = self.prev
                self.second_mistake = node
            self.prev = node

            inorder(node.right)

        self.prev = None
        self.first_mistake, self.second_mistake = None, None

        inorder(root)

        self.first_mistake.val, self.second_mistake.val = self.second_mistake.val, self.first_mistake.val

    def recoverTreeSol5(self, root):
        stack = []
        curr = root
        prev = TreeNode(float('-inf'))
        first_mistake, second_mistake = None, None
        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if not first_mistake and prev.val >= curr.val:
                first_mistake = prev
            if first_mistake and prev.val >= curr.val:
                second_mistake = curr
            prev = curr
            curr = curr.right

        first_mistake.val, second_mistake.val = second_mistake.val, first_mistake.val

    def recoverTreeSol6(self, root):
        stack = []
        curr = root
        prev = None
        out_of_order = []
        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if prev and prev.val >= curr.val:
                out_of_order.append((prev, curr))
            prev = curr
            curr = curr.right

        first, last = out_of_order[0][0], out_of_order[-1][1]
        first.val, last.val = last.val, first.val
