class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        res=0

        h=[i for i in sticks]
        heapq.heapify(h)

        while len(h)>1:
            o=heapq.heappop(h)
            t=heapq.heappop(h)

            res+=o+t
            heapq.heappush(h,o+t)

        return res