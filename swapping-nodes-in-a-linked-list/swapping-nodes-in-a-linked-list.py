# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

       

        firstNode  = head

        for i in range(k-1):
            firstNode = firstNode.next

        dummy = ListNode(-1)
        dummy.next=head
        slow=dummy
        fast=dummy

        for i in range(k):
            fast=fast.next

        while fast is not None:
            slow=slow.next
            fast=fast.next
        print(firstNode.val, slow.val)

        firstNode.val, slow.val = slow.val, firstNode.val

        return head