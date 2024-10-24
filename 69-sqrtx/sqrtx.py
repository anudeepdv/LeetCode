class Solution:
    def mySqrt(self, x: int) -> int:
        
        l =0 
        r=x//2+1
        res=0
        while l<=r:
            m=(l+r)//2
            if m*m==x:
                return m
            elif m*m>x:
                r=m-1
            else:
                res=m
                l=m+1

        return res
            