"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return
        cur = root
        nxt = cur.left

        while cur and nxt:

            if cur.right:
                cur.left.next = cur.right

            if cur.next:
                cur.right.next = cur.next.left
                cur=cur.next
            else:
            
                cur=nxt
                nxt=cur.left    

        return root