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
        cur= dummy


        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            temp=second.next

            cur.next = second
            second.next  =first
            first.next = temp

            cur = first

        return dummy.next