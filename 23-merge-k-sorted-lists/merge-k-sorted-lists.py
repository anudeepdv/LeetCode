# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(h, (lists[i].val,i))
                lists[i]=lists[i].next


        dummy = ListNode(-1)
        cur=dummy
        while h:

            val , index = heappop(h)
            Node = ListNode(val)
            cur.next=Node
            cur=Node

            if lists[index]:
                heappush(h, (lists[index].val,index))
                lists[index]=lists[index].next

        return dummy.next

        