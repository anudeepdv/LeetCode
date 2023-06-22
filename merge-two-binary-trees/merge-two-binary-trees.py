# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 is None and root2 is None:
            return None
        
        v1 = root1.val if root1 is not None else 0
        v2 = root2.val if root2 is not None else 0


        r= TreeNode(v1+v2)
        
        r.left= self.mergeTrees(root1.left if root1 is not None else None,root2.left if root2 is not None else None )
        r.right= self.mergeTrees(root1.right if root1 is not None else None,root2.right if root2 is not None else None )

        return r


