class Node:
     def __init__(self, key, val):
         self.key=key
         self.val=val
         self.prev=self.next=None


class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.c=capacity
        self.left = Node(0,0)
        self.right= Node(0,0)
        self.left.next =self.right
        self.left.prev=None

        self.right.prev =self.left
        self.right.next=None
        
    def remove(self, node:Node):
        l = node.prev
        r=node.next
        l.next = r
        r.prev=l
    
        return node

    def addFromBegining(self, node:Node) -> None:
        node.next=self.left.next
        node.prev=self.left
        self.left.next.prev=node
        self.left.next=node
   
        
        return

    def get(self, key: int) -> int:
        if key in self.hashmap:
            removedNode=self.remove(self.hashmap[key])
            self.addFromBegining(removedNode)
            return self.hashmap[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            removedNode=self.remove(self.hashmap[key])
            del self.hashmap[removedNode.key]

        if(self.c == len(self.hashmap)):
            removedNode=self.remove(self.right.prev)
            del self.hashmap[removedNode.key]

        newNode = Node(key,value)
        self.addFromBegining(newNode)
        self.hashmap[newNode.key]=newNode

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)