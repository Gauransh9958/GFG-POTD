class Solution:

    def findMaxSum(self, arr):
        n = len(arr)

        if n == 0:
            return 0
        if n == 1:
            return arr[0]

        secondLast = 0
        last = arr[0]

        res = 0
        for i in range(1, n):
            res = max(arr[i] + secondLast, last)
            secondLast = last
            last = res

        return res
