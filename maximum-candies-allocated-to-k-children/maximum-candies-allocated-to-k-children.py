class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        l=1
        r=max(candies)
        res=0
        while l<=r:
            m=(l+r)//2
            # print(m)

            childernServed=0
            for i in candies:
                childernServed=childernServed+i//m

            if childernServed>=k:
                l=m+1
                res=m

            else:
                r=m-1

        return res