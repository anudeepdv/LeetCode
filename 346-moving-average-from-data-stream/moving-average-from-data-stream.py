class MovingAverage:

    def __init__(self, size: int):
        self.q = []
        self.size =size
        

    def next(self, val: int) -> float:
        self.q.append(val)

        return sum(self.q[-self.size:])/len(self.q[-self.size:])
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)