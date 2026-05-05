class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0
        for r in range(1, len(prices)):
            maxP = max(maxP, (prices[r] - prices[l]))
            if prices[r] < prices[l]:
                l = r
        return maxP