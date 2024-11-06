class Solution:
    def treePathsSum(self, root):
        return self.calculatePathSum(root, 0)

    def calculatePathSum(self, node, currentSum):
        if node is None:
            return 0

        currentSum = 10 * currentSum + node.data

        if node.left is None and node.right is None:
            return currentSum

        leftSum = self.calculatePathSum(node.left, currentSum)
        rightSum = self.calculatePathSum(node.right, currentSum)

        return leftSum + rightSum
