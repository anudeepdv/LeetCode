class Solution:
    def trap(self, height: List[int]) -> int:
        
        res=0

        maxl,maxr = height[0],height[-1]

        l=0
        r=len(height)-1

        while l<r:

            if maxl<maxr:
                l+=1
                trap = maxl - height[l]
                if trap>0:
                    res+=trap
                maxl = max(maxl,height[l])
                
            else:
                r-=1
                trap = maxr -height[r]
                if trap>0:
                    res+=trap
                maxr = max(maxr,height[r])
                

        return res