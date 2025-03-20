from typing import List


class Solution:

    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        curr = [[0] * 2 for _ in range(3)]
        next = [[0] * 2 for _ in range(3)]

        for i in range(n - 1, -1, -1):
            for k in range(1, 3):

                curr[k][1] = max(-prices[i] + next[k][0], next[k][1])

                curr[k][0] = max(prices[i] + next[k - 1][1], next[k][0])

            
            next = [row[:] for row in curr]

    
        return curr[2][1]