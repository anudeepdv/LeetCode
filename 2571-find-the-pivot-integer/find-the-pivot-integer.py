class Solution:
    def pivotInteger(self, n: int) -> int:
        
        res=-1

        l=1
        r=n

        tot = n*(n+1)//2

        while l<=r:

            m=(l+r)//2
            lsum =  (m - 1 + 1) * (m + 1) // 2
            rsum =  (n - m + 1) * (m + n) // 2

            if lsum==rsum:
                return m
            elif lsum>rsum:
                r=r-1
            else:
                l=l+1

        return -1

