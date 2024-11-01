# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    # Convert the given linked list to an array
    def mapListToValues(self, head: ListNode) -> list:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals

    def sortedListToBST(self, head: ListNode) -> TreeNode:

        # Form an array out of the given linked list and then
        # use the array to form the BST.
        values = self.mapListToValues(head)

        # l and r represent the start and end of the given array
        def convertListToBST(l: int, r: int) -> TreeNode:

            if l>r:
                return None
            
            m =(l+r)//2

            node = TreeNode(values[m])

            if l==r:
                return node

            node.left = convertListToBST(l,m-1)
            node.right = convertListToBST(m+1,r)

            return node

            

        return convertListToBST(0, len(values) - 1)