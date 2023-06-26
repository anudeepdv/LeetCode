class Solution:
    def arrangeCoins(self, n: int) -> int:

        l=0

        r= n
        res=0
        while l<=r:

            m = (l+r)//2

            v=m*(m+1)//2
            if v<=n:
                res=m
                l=m+1
            else:
                r=m-1

        return res