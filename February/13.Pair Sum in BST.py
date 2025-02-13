

class Solution:
    def inorderTraversal(self, root, inorder):
        if root is None:
            return

        self.inorderTraversal(root.left, inorder)

        inorder.append(root.data)

        self.inorderTraversal(root.right, inorder)

    def findTarget(self, root, target):
        inorder = []
        self.inorderTraversal(root, inorder)

        left, right = 0, len(inorder) - 1

        while left < right:
            currentSum = inorder[left] + inorder[right]

            if currentSum == target:
                return True

            if currentSum < target:
                left += 1

            else:
                right -= 1

        return False