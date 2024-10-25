# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next is None:
            return head

        node1= head
        node2= head.next

        while node2:

            a= node1.val
            b = node2.val

            while b!=0:
                a,b = b,a%b
            
            gcdNode = ListNode(a)
            node1.next =gcdNode
            gcdNode.next=node2

            node1 = node2
            node2=node2.next

        return head