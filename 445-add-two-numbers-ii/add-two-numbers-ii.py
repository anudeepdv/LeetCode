# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        q1= collections.deque()

        while l1:
            q1.append(l1)
            l1=l1.next

        q2= collections.deque()

        while l2:
            q2.append(l2)
            l2=l2.next

        head = ListNode(-1)

        tot,carr=0,0

        while q1 or q2:

            if q1:
                tot+=q1.pop().val
               
            if q2:
                tot+=q2.pop().val
            # print(tot)

            ans=tot%10
            n = ListNode(ans)
            n.next=head.next
            head.next=n
            carry=tot//10
            tot=carry
        print(tot)
        if tot:
            n = ListNode(tot)
            n.next=head.next
            head.next=n

        return head.next


