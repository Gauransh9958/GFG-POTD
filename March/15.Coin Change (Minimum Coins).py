class Solution:

    def minCoins(self, coins, sum):
        dp = [[0] * (sum + 1) for _ in range(len(coins))]

        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, sum + 1):
                dp[i][j] = float('inf')
                take = float('inf')
                noTake = float('inf')

                if j - coins[i] >= 0:
                    take = dp[i][j - coins[i]]
                    if take != float('inf'):
                        take += 1

                if i + 1 < len(coins):
                    noTake = dp[i + 1][j]

                dp[i][j] = min(take, noTake)

        if dp[0][sum] != float('inf'):
            return dp[0][sum]
        return -1