class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.first,self.last=Node(0,0),Node(0,0)
        self.first.next=self.last
        self.last.prev=self.first
        self.map={}
        self.capacity=capacity
        
    def remove(self,node):
        l,r =node.prev,node.next
        l.next=r
        r.prev=l
        node.prev=l
        node.next=r


    def add(self,node):
        l=self.last.prev

        l.next=node
        self.last.prev=node
        node.prev=l
        node.next=self.last

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.add(self.map[key])
            return self.map[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            del self.map[key]
        node=Node(key,value)
        self.map[key]=node
        self.add(node)

        if len(self.map)>self.capacity:
            first = self.first.next
            del self.map[first.key]
            self.remove(first)
           




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)