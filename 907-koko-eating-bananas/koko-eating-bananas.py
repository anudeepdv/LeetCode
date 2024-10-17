class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l =1
        r= max(piles)

        res=math.inf

        while l<=r:

            m = (l+r)//2
            time=0
            for i in piles:
                time = time+math.ceil(i/m)

            if time >h:
                l=m+1
            else:
                res=min(res,m)
                r=m-1

        return res

            