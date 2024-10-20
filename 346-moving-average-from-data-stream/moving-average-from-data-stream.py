class MovingAverage:

    def __init__(self, size: int):
        self.q=deque()
        self.size = size
        self.window=0


    def next(self, val: int) -> float:
        
        self.q.append(val)
        left = 0 if len(self.q)<=self.size else self.q.popleft()
        print(left)
        self.window = self.window + val -left

        return self.window/min(self.size,len(self.q))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)