class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        b=prices[0]
        best = 0

        for s in prices[1:]:

            best  = max(best,s-b)
            if s<b:
                b=s

        return best