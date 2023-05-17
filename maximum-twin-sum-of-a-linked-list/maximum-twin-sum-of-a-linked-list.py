# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        temp1 = head
        temp2 = head
        arr =[]
        while temp2 is not None:
            arr.append(temp1.val)
            temp1= temp1.next
            temp2 = temp2.next.next

        print(arr, temp1.val)
        i=0
        while temp1 is not None:
            arr[-i-1] =arr[-i-1]+ temp1.val
            temp1= temp1.next
            i=i+1

        return max(arr)