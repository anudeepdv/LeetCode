class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:      
      
        h = []

        for i in nums:
            if len(h)<k:
                heappush(h, i)

            else:
                if i>h[0]:
                    heappop(h)
                    heappush(h, i)

        return h[0]
