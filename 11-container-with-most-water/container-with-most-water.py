class Solution:
    def maxArea(self, height: List[int]) -> int:

        l=0
        r=len(height)-1
        res=0
        while l<r:

            h = min(height[l],height[r])

            area = h*(r-l)
            res = max(res,area)
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1

        return res