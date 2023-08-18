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
        
        cur= head
        d={}
        f=Node(-1)
        prev=f
        while cur:
            print(cur.val)
            dup=Node(cur.val)
            d[cur]=dup

            prev.next=dup
            prev=dup
            cur=cur.next

        
        
        cur=head

        for i in d:
            dup= d[i]
            rc = i.random
            if rc is not None:
                rd=d[rc]
                dup.random=rd
        return f.next




            


