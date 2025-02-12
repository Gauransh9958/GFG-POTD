class Solution:

    def kthSmallest(self, root, k):
        ksmall = -1
        curr = root

        while curr != None:


            if curr.left == None:
                if k == 1:
                    ksmall = curr.data
                k -= 1
                curr = curr.right

            else:
                pre = curr.left

                while pre.right != None and pre.right != curr:
                    pre = pre.right

                if pre.right == None:
                    pre.right = curr
                    curr = curr.left

                else:

                    if k == 1:
                        ksmall = curr.data
                    k -= 1
                    pre.right = None
                    curr = curr.right

        return ksmall