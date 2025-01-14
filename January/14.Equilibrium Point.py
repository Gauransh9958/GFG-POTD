class Solution:

    def findEquilibrium(self, arr):
        n = len(arr)
        sum = 0
        for i in range(0, n):
            sum += arr[i]
        sum2 = 0

        for i in range(0, n, +1):

            sum -= arr[i]

            if sum2 == sum:
                return i

            sum2 += arr[i]

        return -1