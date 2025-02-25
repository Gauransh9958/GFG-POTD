

class Solution:
    # Function to calculate the maximum rectangular area
    def getMaxArea(self, arr):
        n = len(arr)
        s = []
        res = 0

        for i in range(n):

            # Process the stack while the current element
            # is smaller than the element corresponding to
            # the top of the stack
            while s and arr[s[-1]] >= arr[i]:

                # The popped item is to be considered as the
                # smallest element of the Histogram
                tp = s.pop()

                # For the popped item, the previous smaller
                # element is just below it in the stack (or
                # the current stack top) and the next smaller
                # element is i
                width = i if not s else i - s[-1] - 1

                # Update the result if needed
                res = max(res, arr[tp] * width)

            s.append(i)

        # For the remaining items in the stack, next smaller does
        # not exist. Previous smaller is the item just below in
        # the stack.
        while s:
            tp = s.pop()
            width = n if not s else n - s[-1] - 1
            res = max(res, arr[tp] * width)

        return res