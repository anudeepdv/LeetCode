# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        found=[False]
        def dfs(node,res):
            if not node :
                return 

            res+=node.val

            if not node.left and not node.right and res==targetSum:
                found[0]=True
                return

            dfs(node.left, res)
            dfs(node.right, res)

            return 

        dfs(root,0)
        return found[0]