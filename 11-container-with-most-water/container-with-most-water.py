class Solution:
    def maxArea(self, height: List[int]) -> int:
        l =0 
        r =len(height)-1
        maxy=0
        
        while l<r:

            dist = r-l
            area=min(height[r],height[l])*dist
            maxy=max(area,maxy)

            if height[r]>height[l]:
                l=l+1
            else:
                r=r-1

        return maxy