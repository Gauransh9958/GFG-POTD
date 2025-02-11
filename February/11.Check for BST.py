

class Solution:

    INT_MAX = 4294967296
    INT_MIN = -4294967296

    def isBST(self, node):
        return (self.isBSTUtil(node, self.INT_MIN, self.INT_MAX))

    def isBSTUtil(self, node, mini, maxi):

        if node is None:
            return True

        if node.data < mini or node.data > maxi:
            return False

        return (self.isBSTUtil(node.left, mini, node.data - 1)
                and self.isBSTUtil(node.right, node.data + 1, maxi))