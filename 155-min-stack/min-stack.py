class MinStack:

    def __init__(self):
        self.minh=collections.deque()
        self.h=collections.deque()

    def push(self, val: int) -> None:
        if len(self.h)==0:
            self.minh.append(val)
            self.h.append(val)

        else:
            m = min(val,self.minh[-1]) 
            self.minh.append(m)
            self.h.append(val)

    def pop(self) -> None:
        self.minh.pop()
        self.h.pop()

    def top(self) -> int:
        return self.h[-1]

    def getMin(self) -> int:
        return self.minh[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()