class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h=[]
        heapq.heapify(h)
        for i in range(len(heights)-1):
            diff = heights[i+1]-heights[i]

            if diff<0:
                continue
            
            heapq.heappush(h,diff)

            if len(h)<=ladders:
                continue
            
            pop = heapq.heappop(h)

            bricks=bricks-pop
            if bricks<0:
                return i
            
        return len(heights)-1

            
        