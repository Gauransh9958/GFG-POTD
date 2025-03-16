class Solution:

    def minJumps(self, arr):
        n = len(arr)

        dp = [float('inf')] * n
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, min(i + arr[i] + 1, n)):
                if dp[j] != float('inf'):
                    dp[i] = min(dp[i], 1 + dp[j])

        if dp[0] == float('inf'):
            return -1

        return dp[0]