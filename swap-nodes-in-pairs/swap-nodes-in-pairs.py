# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy.next
        prev=dummy

        while curr is not None and curr.next is not None:
           
          
            secondCurr = curr.next

            temp=prev.next
            prev.next=curr.next
            curr.next =secondCurr.next
            secondCurr.next=temp
            prev=curr
            curr=curr.next

        return dummy.next
        
