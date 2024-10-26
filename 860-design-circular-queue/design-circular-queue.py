class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head=None
        self.tail=None
        self.cap=k
        self.k =0
        
    def enQueue(self, value: int) -> bool:
        if self.head==self.tail==None:
            self.k+=1
            self.head=self.tail=Node(value)
            return True
        if self.k <self.cap:
            self.tail.next=Node(value)
            self.tail =self.tail.next
            self.k+=1
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if self.k>0:
            node = self.head

            self.head=self.head.next
            if self.k==1:
                self.tail =None

            self.k-=1
            return True

        else:
            return False
        

    def Front(self) -> int:
        if self.k>0:
            return self.head.val
        else:
            return -1
        

    def Rear(self) -> int:
        if self.k>0:
            return self.tail.val
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.k==0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.k==self.cap:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()