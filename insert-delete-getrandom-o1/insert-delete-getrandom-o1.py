class RandomizedSet:

    def __init__(self):
        self.dict={}
        self.stack=[]
        

    def insert(self, val: int) -> bool:
        
        if val in self.dict:
            return False
        
        self.dict[val]=len(self.stack)
        self.stack.append(val)

        return True

    def remove(self, val: int) -> bool:

        if val not in self.dict:
            return False
        # print(self.dict,self.stack,val)
        idx=self.dict[val]
        self.stack[idx]= self.stack[-1]
        pop = self.stack.pop()
        self.dict[pop]=idx
        del self.dict[val]
        # print(self.dict,self.stack)

        return True
        
        

    def getRandom(self) -> int:
        # choice = random.choice(0,len(self.stack))
        return random.choice(self.stack)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()