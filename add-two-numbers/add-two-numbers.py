# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        carry=0
        curr=dummy
        while (l1 is not None or l2 is not None):

            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0

            num3 = num1 +num2+carry
            carry, val = divmod(num3, 10)
            curr.next=ListNode(val)
            curr= curr.next

            if l1:
                l1=l1.next

            if l2:
                l2=l2.next

        if carry:
            curr.next=ListNode(carry)
            curr= curr.next

        return dummy.next
            







        