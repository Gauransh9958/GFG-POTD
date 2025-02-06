class Solution:

    def buildIndexMap(self, inorder):
        indexMap = {}
        for index, value in enumerate(inorder):
            indexMap[value] = index
        return indexMap

    def buildUtil(self, inorder, preorder, inStart, preStart, n, indexMap):
        if n <= 0:
            return None

        root = Node(preorder[preStart])

        i = indexMap[preorder[preStart]]

        leftSubtreeSize = i - inStart

        root.left = self.buildUtil(inorder, preorder, inStart, preStart + 1,
                                leftSubtreeSize, indexMap)
        root.right = self.buildUtil(inorder, preorder, i + 1,
                                    preStart + leftSubtreeSize + 1,
                                    n - leftSubtreeSize - 1, indexMap)

        return root

    def buildTree(self, inorder, preorder):
        indexMap = self.buildIndexMap(inorder)
        n = len(inorder)
        return self.buildUtil(inorder, preorder, 0, 0, n, indexMap)