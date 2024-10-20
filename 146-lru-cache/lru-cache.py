class Node:

    def __init__(self,key,val):
        self.key = key
        self.val =val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(-1,-1)
        self.right = Node(-1,-1)
        self.left.next = self.right
        self.right.prev=self.left
        self.m={}
        self.capacity=capacity

    def addbegining(self, node: Node) -> None :
        temp = self.left.next
        self.left.next = node
        node.prev= self.left
        node.next=temp
        temp.prev=node

    def remove(self, node: Node) -> None :

        nodel = node.prev
        noder=node.next
        nodel.next = noder
        noder.prev=nodel


    def get(self, key: int) -> int:

        if key in self.m:

            node = self.m[key]
            self.remove(node)
            self.addbegining(node)

            return node.val

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # print(key,value)
        if key in self.m:
            node = self.m[key]
            node.val = value
            self.remove(node)
            self.addbegining(node)

        else:
            if len(self.m)==self.capacity:
                temp  = self.right.prev
                del self.m[temp.key]
                self.remove(temp)
                node=Node(key,value)
                self.addbegining(node)
                self.m[key]=node         
            else:
                node=Node(key,value)
                self.addbegining(node)
                self.m[node.key]=node

        # print(self.m.keys())

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)