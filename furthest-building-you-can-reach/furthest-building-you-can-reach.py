class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        h =[]
        heapq.heapify(h)
        n=len(heights)
        for i in range(n-1):
            diff = heights[i+1] -heights[i]
            if diff<=0:
                continue

            heapq.heappush(h,diff)

            if len(h)<=ladders:
                continue
            
            pop = heapq.heappop(h)

            bricks = bricks-pop
            if bricks<0:
                return i
        return n-1

