class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l =1
        r= max(piles)

        res = r

        while(l<=r):
            
            m = (l+r)//2

            hours=0
            for i in piles:
                hours =hours+ math.ceil(i/m)

            if hours<=h:
                res=min(res,m)
                r=m-1

            else:
                l=m+1

        return res