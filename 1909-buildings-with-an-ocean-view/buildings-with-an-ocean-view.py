class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        res= []
        maxh = 0

        for  i in range(len(heights)-1,-1,-1):
            if heights[i]>maxh:
                res.append(i)
                maxh=heights[i]
        return res[::-1]