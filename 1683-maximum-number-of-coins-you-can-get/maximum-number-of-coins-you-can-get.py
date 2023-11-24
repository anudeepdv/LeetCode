class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        l=0
        r=len(piles)-1

        res=0

        while l<r:
            r=r-1
            res+=piles[r]
            r=r-1
            l=l+1

        return res

