# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        s=[]
        while head:
            s.append(head)
            head=head.next

        for i in range(len(s)-1,-1,-1):
            if s[i].val==9:
                s[i].val=0
                if i==0:
                    
                    return ListNode(1,s[i])
            else:
                s[i].val+=1
                return s[0]
