# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        cur=dummy
        c=0
        while l1 or l2:
            v1= l1.val if l1 else 0
            v2= l2.val if l2 else 0

            s = v1+v2+c

            val = s%10
            c=s//10

            node = ListNode(val)
            cur.next=node
            cur=cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if c:
            node = ListNode(c)
            cur.next=node


        return dummy.next     

