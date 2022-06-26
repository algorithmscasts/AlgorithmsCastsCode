class Solution:
    def averageOfSubtree(self, root):
        def dfs(node):
            if not node:
                return (0, 0)

            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)

            newSum, newCount = leftSum + rightSum + node.val, leftCount + rightCount + 1
            if node.val == (newSum // newCount):
                self.count += 1
            return (newSum, newCount)

        self.count = 0
        dfs(root)
        return self.count


