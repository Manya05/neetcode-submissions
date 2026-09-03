class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit =0

        for i in range(1,len(prices)):
            minPrice = min(minPrice, prices[i-1])
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit