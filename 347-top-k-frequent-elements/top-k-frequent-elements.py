class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)
        h = []
        for key,v in c.items():
            heapq.heappush(h, (-v,key))
        res = []
        for i in range(k):
            res.append(heappop(h)[1])
        return res