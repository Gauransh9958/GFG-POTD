class Solution:
    def correctBSTUtil(self, root, first, middle, last, prev):
        if root is None:
            return

        self.correctBSTUtil(root.left, first, middle, last, prev)

        if prev[0] is not None and root.data < prev[0].data:
            if first[0] is None:
                first[0] = prev[0]
                middle[0] = root
            else:
                last[0] = root

        prev[0] = root

        self.correctBSTUtil(root.right, first, middle, last, prev)

    def correctBST(self, root):
        first = [None]
        middle = [None]
        last = [None]
        prev = [None]

        self.correctBSTUtil(root, first, middle, last, prev)

        if first[0] and last[0]: 
            first[0].data, last[0].data = last[0].data, first[0].data
        elif first[0] and middle[0]: 
            first[0].data, middle[0].data = middle[0].data, first[0].data