class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h=[]
        self.k=k
        for i in nums:
            if len(self.h)<k:
                heappush(self.h, i)
            else:
                if i > self.h[0]:
                    heappushpop(self.h, i)
        # print(self.h)

        

    def add(self, val: int) -> int:
        if len(self.h)<self.k:
            heappush(self.h, val)
        else:
            if val >= self.h[0]:
                heappop(self.h)
                heappush(self.h, val)
        # print(self.h)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)