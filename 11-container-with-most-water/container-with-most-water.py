class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l =0 
        r=len(height)-1
        res=0
        while l<r:

            res = max(res,min(height[l],height[r])*(r-l))

            if height[l]<=height[r]:
                l=l+1
            else:
                r=r-1

        return res


            