class Solution:

    def inOrder(self, root):
        res = []
        curr = root

        while curr is not None:
            if curr.left is None:


                res.append(curr.data)
                curr = curr.right
            else:

                prev = curr.left
                while prev.right is not None \
                and prev.right != curr:
                    prev = prev.right


                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:


                    prev.right = None
                    res.append(curr.data)
                    curr = curr.right

        return res