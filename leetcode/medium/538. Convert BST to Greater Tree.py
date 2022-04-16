class Solution:

    def convertBST(self, root):
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            self.values.append(node.val)
            inorder(node.right)

        def update(node):
            if not node:
                return

            update(node.right)
            node.val = self.values.pop()
            update(node.left)

        self.values = []
        inorder(root)

        for i in range(len(self.values) - 2, -1, -1):
            self.values[i] += self.values[i + 1]

        update(root)
        return root

    def convertBSTSol2(self, root):

        # reverse inorder traversal
        def update(node):
            if not node:
                return

            update(node.right)

            self.suffix_sum += node.val
            node.val = self.suffix_sum
            update(node.left)

        self.suffix_sum = 0

        update(root)
        return root
