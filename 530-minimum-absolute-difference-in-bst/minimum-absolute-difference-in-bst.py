# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        prev =None
        res=math.inf
        def inorder(node):
            nonlocal prev
            nonlocal res
            if not node:
                return
            inorder(node.left)

            val = node.val
            print(val,prev)
            if  prev is not None:
                
                res = min(res,abs(prev-val))
    
            prev=val
            inorder(node.right)

        inorder(root)

        return res
