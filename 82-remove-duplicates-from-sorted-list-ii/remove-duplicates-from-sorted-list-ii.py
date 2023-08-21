# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-101,head)

        prev=dummy
        cur=head

        while cur and cur.next:

            f=False
            print(prev.val,cur.val)
            print('hi')
            while cur and cur.next and cur.val==cur.next.val:
                print(cur.val,cur.next.val)
                cur=cur.next
                f=True

            print('--')
            if f:
                cur=cur.next
                prev.next=cur
            else:
                prev=prev.next
                cur=cur.next



        return dummy.next