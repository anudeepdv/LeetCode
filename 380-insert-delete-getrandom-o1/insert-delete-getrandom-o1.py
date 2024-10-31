class RandomizedSet:

    def __init__(self):
        self.l = deque()
        self.map = {}
        
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val]=len(self.l)
        self.l.append(val)

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        index =self.map[val]
        lastelement = self.l[-1]
        self.l[index]=lastelement
        self.map[lastelement]= index
        self.l.pop()
        del self.map[val]
        return True

        

    def getRandom(self) -> int:
        return random.choice(self.l)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()