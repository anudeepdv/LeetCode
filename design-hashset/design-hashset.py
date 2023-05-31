class Node:
    def __init__(self,value):
        self.val=value
        self.next=None


class MyHashSet:

    def __init__(self):  
        self.keyStore= [Node(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        hashed = key%len(self.keyStore)
        cur = self.keyStore[hashed]  
        while cur.next:
            if cur.next.val ==key:
                return
            cur=cur.next      
        cur.next = Node(key)

    def remove(self, key: int) -> None:
        hashed = key%len(self.keyStore)
        cur = self.keyStore[hashed]
        while cur.next:
            if cur.next.val ==key:
                cur.next=cur.next.next
                return
            cur=cur.next
  
    def contains(self, key: int) -> bool:
        hashed = key%len(self.keyStore)
        cur = self.keyStore[hashed]
        while cur.next:
            if cur.next.val ==key:
                return True
            cur=cur.next
        return False
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)