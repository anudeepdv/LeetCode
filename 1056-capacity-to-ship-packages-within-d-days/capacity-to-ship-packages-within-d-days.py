class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        

        l= max(weights)
        r= sum(weights)
        res=0

        def can_ship(w):
            d=1
            s=0
            for i in weights:
                if s+i <= w:
                    s+=i
                else:
                    s=i
                    d+=1
            # print(w,d)
            return d

        while l<=r:

            m = (l+r)//2

            if (can_ship(m)<=days):
                res=m
                r=m-1
            else:
                l=m+1

        return res