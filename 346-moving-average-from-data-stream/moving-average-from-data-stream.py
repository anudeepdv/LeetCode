class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.window = 0
        self.size = size
        

    def next(self, val: int) -> float:

        self.q.append(val)

        left = self.q.popleft() if len(self.q)>self.size else 0

        self.window+= -left +val

        return self.window/len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)