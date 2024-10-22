# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        def dfs(treenode,listnode):
            if not listnode:
                return True

            if not treenode:
                return False

            if treenode.val!=listnode.val:
                return False

            return dfs(treenode.left, listnode.next) or dfs(treenode.right, listnode.next)

        return dfs(root,head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)