class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class MyHashMap:

    def __init__(self):
         self.keyStore= [Node(-1,-1) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:

        hashed = key%10**4
        cur = self.keyStore[hashed]
        found=False
        while cur.next:
            if cur.next.key==key:
                cur.next.value=value
                found=True
                break
            cur=cur.next

        if found is False:
            cur.next= Node(key,value)

            
        

    def get(self, key: int) -> int:
        hashed = key%10**4
        cur = self.keyStore[hashed]
        found=False
        while cur.next:
            if cur.next.key==key:
                return cur.next.value
            cur=cur.next

        return -1

    def remove(self, key: int) -> None:
        hashed = key%10**4
        cur = self.keyStore[hashed]
        found=False
        while cur.next:
            if cur.next.key==key:
                cur.next=cur.next.next
                break
            cur=cur.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)