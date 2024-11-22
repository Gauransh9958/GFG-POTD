class Solution:
    def maximumProfit(self, prices):
        # Edge case: if there are less than 2 prices, no transaction is possible
        if len(prices) < 2:
            return 0
        
        # Initialize variables:
        min_price = prices[0]  # Start with the first price as the minimum price
        max_profit = 0  # Initially no profit

        # Iterate through the prices starting from the second day
        for price in prices:
            # Calculate profit if we sell at the current price and buy at min_price
            profit = price - min_price
            # Update max_profit if this profit is greater than the previously recorded max profit
            max_profit = max(max_profit, profit)
            # Update min_price if the current price is lower than the min_price
            min_price = min(min_price, price)

        return max_profit