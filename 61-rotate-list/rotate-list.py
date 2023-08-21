# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if  head is None or k==0 or head.next is None:
            return head

        l=1
        cur=head
        while cur.next:
            l=l+1
            cur=cur.next
        print(l)

        slow=head
        fast=head

        k=k%l
        if k:
            for i in range(k):
                fast=fast.next
            
            while fast.next:
                slow=slow.next
                fast=fast.next

            print(slow.val,fast.val)

            newh = slow.next
            slow.next=None
            fast.next=head
            return newh
        return head