# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def func1(r, s):

            if r is None:
                return False
            if s is None: return True

            if checkSame(r,s):
                return True
            
            return func1(r.left,s) or func1(r.right,s)

        def checkSame(r,s):

            if r is None and s is not None:
                return False
            if r is not None and s is  None:
                return False
            if r is None and s is  None:
                return True
            if r and s and r.val == s.val:
                return checkSame(r.left,s.left) and checkSame(r.right,s.right)

            return False


        return func1(root,subRoot)