class Solution:
    def maximumProfit(self, prices):
        if len(prices) < 2:
            return 0
        
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)

        return max_profit