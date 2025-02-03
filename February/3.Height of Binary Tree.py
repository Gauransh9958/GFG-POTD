

class Solution:

    def height(self, node):

        if node is None:
            return -1

        return (1 + max(self.height(node.left), self.height(node.right)))