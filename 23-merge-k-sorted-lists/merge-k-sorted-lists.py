# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        h = []

        for i,node in enumerate(lists):
            if node:
                heappush(h,(node.val,i))
        print(h)
        dummy = ListNode(-1)
        cur = dummy

        while h:

            val, i = heappop(h)
            cur.next = lists[i]
            cur = cur.next
            lists[i]=lists[i].next
            if lists[i]:
                heappush(h,(lists[i].val,i))

        return dummy.next