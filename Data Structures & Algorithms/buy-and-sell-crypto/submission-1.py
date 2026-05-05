class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = float('-inf')
        for r in range(len(prices)):
            maxP = max(maxP, (prices[r] - prices[l]))
            if prices[r] < prices[l]:
                l = r
        return maxP