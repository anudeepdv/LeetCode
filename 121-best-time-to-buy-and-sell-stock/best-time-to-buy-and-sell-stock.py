class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        b = prices[0]
        res=0
        for s in prices[1:]:

            res =max(res,s-b)
            if s<b:
                b=s

        return res

        