"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy= Node(-1)
        d={}
        cur =head
        pd = dummy
        while cur:
            
            newnode=None
            if cur in d:
                newnode = d[cur]
                pd.next=newnode
            else:
                newnode=Node(cur.val)
                d[cur]=newnode
                pd.next=newnode
            pd=newnode
            rand = cur.random

            if rand in d:
                randNoded = d[rand]
                newnode.random=randNoded
            elif rand is not None:
                randNoded=Node(rand.val)
                d[rand]=randNoded
                newnode.random=randNoded
            
            cur=cur.next

        return dummy.next


