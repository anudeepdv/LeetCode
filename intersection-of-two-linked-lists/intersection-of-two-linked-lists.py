# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        stack1 =  collections.deque()
        stack2 = collections.deque()
        while headA is not None or headB is not None:
            if headA:
                stack1.append(headA)
                headA=headA.next
            if headB:
                stack2.append(headB)
                headB=headB.next

        match=None

        while stack1 and stack2:

            a= stack1.pop()
            b= stack2.pop()

            if a!=b:
                return match
            else:
                match =a

        return match
                

