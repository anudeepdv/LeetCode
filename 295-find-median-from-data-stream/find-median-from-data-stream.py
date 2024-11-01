class MedianFinder:

    def __init__(self):
        self.maxh = []
        self.minh= []
        self.c=0
        

    def addNum(self, num: int) -> None:
        heappush(self.maxh, -num)
        heappush(self.minh, -heappop(self.maxh))
        if len(self.minh)>len(self.maxh):
            heappush(self.maxh, -heappop(self.minh))
        self.c+=1

    def findMedian(self) -> float:

        if self.c%2==0:
            return (-self.maxh[0] + self.minh[0])/2
        else:
            return -self.maxh[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()