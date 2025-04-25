class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force is to calculate the price of each combination to buy and sell the stock

        lowest = prices[0]
        profit = 0

        for i in range(len(prices)):
            lowest = min(prices[i], lowest)
            if prices[i] > lowest:
                profit = max(profit, prices[i] - lowest)

        return profit



