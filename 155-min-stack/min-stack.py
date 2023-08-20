class MinStack:

    def __init__(self):
        self.s=[]
        self.m=[]

    def push(self, val: int) -> None:
        if self.s:
            m = min(self.m[-1],val)
            self.s.append(val)
            self.m.append(m)
        else:
            self.s.append(val)
            self.m.append(val)


        

    def pop(self) -> None:
        self.m.pop()
        return self.s.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.m[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()