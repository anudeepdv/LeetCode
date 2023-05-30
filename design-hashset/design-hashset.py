class MyHashSet:

    def __init__(self):
        self.keys=[]
        # self.values=[]
        

    def add(self, key: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
        

    def remove(self, key: int) -> None:
        if key in  self.keys:
            i = self.keys.index(key)
            print(self.keys,i)
            self.keys.pop(i)
        

    def contains(self, key: int) -> bool:
        if key in self.keys:
            return True

        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)