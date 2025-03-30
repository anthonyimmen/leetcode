class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force - calculate every price combination using a nested for loop
        # more efficient - if next day price is less than current day, make that the new

        maxProfit = 0
        startingDay = 0
        currDay = 1

        while currDay < len(prices):
            maxProfit = max(maxProfit, prices[currDay] - prices[startingDay])
            if prices[currDay] < prices[startingDay]:
                startingDay = currDay
            currDay += 1
        return maxProfit
