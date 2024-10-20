class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        curHtg=-1
        res=collections.deque([])
        for i in range(len(heights)-1,-1,-1):
            if curHtg<heights[i]:
                curHtg=heights[i]
                res.appendleft(i)
        return list(res)