# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       
        h=[]
        
        heapq.heapify(h)

        for i in range(len(lists)):
                if lists[i]:
                    heapq.heappush(h, (lists[i].val, i))
                    lists[i]=lists[i].next

        dummy = ListNode(-1)
        cur=dummy
        while len(h)>0:
            element = heapq.heappop(h)
            cur.next=ListNode(element[0])

            if lists[element[1]] is not None:
                heapq.heappush(h,(lists[element[1]].val,element[1]))
                lists[element[1]]= lists[element[1]].next

            cur =cur.next
        return dummy.next

