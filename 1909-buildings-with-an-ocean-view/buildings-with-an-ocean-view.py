class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        curHtg=-1
        res=collections.deque([])
        for i in range(len(heights)-1,-1,-1):
            if heights[i]>curHtg:
                res.appendleft(i)
                curHtg= heights[i]

        return list(res)