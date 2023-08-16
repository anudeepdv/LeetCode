class RandomizedSet:

    def __init__(self):
        self.hashmap={}
        self.l=[]
        

    def insert(self, val: int) -> bool:

        if val in self.hashmap:
            return False

        k = len(self.l)
        self.hashmap[val]=k

        self.l.append(val)

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        ind = self.hashmap[val]
        pop = self.l[-1]
        self.l[ind]=pop
        self.l.pop()
        self.hashmap[pop]=ind
        del self.hashmap[val]  
        return True      

    def getRandom(self) -> int:
        return random.choice(self.l)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()