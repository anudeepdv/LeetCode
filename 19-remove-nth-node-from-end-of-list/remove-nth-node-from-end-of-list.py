# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1,head)
        s=head

        for i in range(n-1):
            s=s.next
        
        print(s.val)
        prev=None
        cur =dummy
        while s:
            s=s.next
            prev=cur
            cur=cur.next

        prev.next = cur.next

        return dummy.next
