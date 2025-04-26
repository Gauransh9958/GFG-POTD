
class Solution:

    # This function counts the number of nodes
    # in a binary tree
    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # This function checks if the binary tree is
    # complete or not
    def isCompleteUtil(self, root, index, numberOfNodes):
        if root is None:
            return True

        # If index assigned to current node is more than
        # number of nodes in the tree, then the tree is not complete
        if index >= numberOfNodes:
            return False

        # Recur for left and right subtrees
        return self.isCompleteUtil(root.left, 2 * index + 1, numberOfNodes) and \
               self.isCompleteUtil(root.right, 2 * index + 2, numberOfNodes)

    # This function checks the heap property in the tree.
    def isHeapUtil(self, root):
        if root.left is None and root.right is None:
            return True

        # Node will be in the second-last level
        if root.right is None:

            # Check heap property at the node
            # No recursive call because no need to check the last level
            return root.data >= root.left.data
        else:

            # Check heap property at the node and recursively
            # check the heap property at left and right subtrees
            if root.data >= root.left.data and root.data >= root.right.data:
                return self.isHeapUtil(root.left) and self.isHeapUtil(
                    root.right)
            else:
                return False

    # Function to check if the binary tree is
    # a Heap or not.
    def isHeap(self, root):
        nodeCount = self.countNodes(root)
        index = 0

        if self.isCompleteUtil(root, index, nodeCount) \
        and self.isHeapUtil(root):
            return True
        return False