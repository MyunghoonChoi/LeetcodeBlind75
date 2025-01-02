class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for ind in range(1,len(prices)):
            sell = prices[ind]
            curProfit = sell - buy
            if curProfit > maxProfit:
                maxProfit = curProfit
            if buy > sell:
                buy = sell
        return maxProfit
