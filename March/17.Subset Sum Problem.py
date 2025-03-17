class Solution:

    def isSubsetSum(self, arr, sum):

        N = len(arr)
        subset = [[False] * (sum + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            subset[i][0] = True

        for i in range(1, sum + 1):
            subset[0][i] = False

        for i in range(1, N + 1):
            for j in range(1, sum + 1):
                if j < arr[i - 1]:
                    subset[i][j] = subset[i - 1][j]
                if j >= arr[i - 1]:
                    subset[i][j] = subset[i - 1][j] or subset[i -
                                                            1][j -
                                                                arr[i - 1]]

        return subset[N][sum]