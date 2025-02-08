class Solution:

    def printLeaves(self, root, res):
        if root is None:
            return

        self.printLeaves(root.left, res)

        if not root.left and not root.right:
            res.append(root.data)

        self.printLeaves(root.right, res)

    def printBoundaryLeft(self, root, res):
        if root is None:
            return

        if root.left:

            res.append(root.data)
            self.printBoundaryLeft(root.left, res)
        elif root.right:
            res.append(root.data)
            self.printBoundaryLeft(root.right, res)


    def printBoundaryRight(self, root, res):
        if root is None:
            return

        if root.right:
            self.printBoundaryRight(root.right, res)
            res.append(root.data)
        elif root.left:
            self.printBoundaryRight(root.left, res)
            res.append(root.data)


    def boundaryTraversal(self, root):
        res = []
        if root is None:
            return res

        res.append(root.data)

        self.printBoundaryLeft(root.left, res)

        self.printLeaves(root.left, res)
        self.printLeaves(root.right, res)

        self.printBoundaryRight(root.right, res)

        return res