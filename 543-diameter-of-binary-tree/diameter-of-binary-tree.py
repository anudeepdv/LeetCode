# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res=0
        def dfs(node):
            nonlocal res
            if not node:
                return -1
            
            l = dfs(node.left)
            r=dfs(node.right)

            res=max(res,2+l+r)

            return 1+max(l,r)

        dfs(root)
        return res