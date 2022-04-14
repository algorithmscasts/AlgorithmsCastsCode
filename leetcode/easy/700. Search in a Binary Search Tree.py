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
