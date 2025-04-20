class Solution:

    def findDuplicate(self, arr):
        n = len(arr)
        res = 0

        for i in range(n - 1):
            res = res ^ (i + 1) ^ arr[i]

        res = res ^ arr[n - 1]

        return res