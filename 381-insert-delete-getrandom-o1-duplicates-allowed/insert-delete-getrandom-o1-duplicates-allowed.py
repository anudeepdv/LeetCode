class RandomizedCollection:

    def __init__(self):
        self.q = collections.deque()
        self.map=collections.defaultdict(set)

        

    def insert(self, val: int) -> bool:


        self.map[val].add(len(self.q))
        self.q.append(val)
    
        return len(self.map[val])==1

        

    def remove(self, val: int) -> bool:

        if len(self.map[val])==0:
            return False

        
        idx = self.map[val].pop()
        lastele = self.q[-1]
        self.q[idx]=lastele
        self.map[lastele].add(idx)
        self.map[lastele].remove(len(self.q)-1)
        self.q.pop()
        return True
        

    def getRandom(self) -> int:
        return choice(self.q)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()