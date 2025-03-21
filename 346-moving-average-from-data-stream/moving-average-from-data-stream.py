class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.window = 0
        self.size = size
        self.count =0
        

    def next(self, val: int) -> float:
        self.count += 1
        self.q.append(val)

        left = self.q.popleft() if self.count>self.size else 0

        self.window+= -left +val

        return self.window/min(self.count,self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)