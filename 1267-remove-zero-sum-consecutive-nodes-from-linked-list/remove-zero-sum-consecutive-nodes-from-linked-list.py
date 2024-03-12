# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy= ListNode(0,head)

        pr_sum=0
        pr_map={}

        cur=dummy.next

        while cur:
            pr_sum+=cur.val
            pr_map[pr_sum]=cur
            cur=cur.next



        cur = dummy
        pr_sum=0

        while cur:
            pr_sum+=cur.val
            if pr_sum in pr_map:
                cur.next = pr_map[pr_sum].next

            cur=cur.next
        return dummy.next

