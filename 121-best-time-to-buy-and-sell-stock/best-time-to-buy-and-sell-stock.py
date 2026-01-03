class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit  = 0
        buy = float(inf)

        for p in prices:
            profit = max(profit,p-buy)
            buy = min(buy,p)
        
        return profit