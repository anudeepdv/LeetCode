# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=[0]
        def dfs(node,r):
            if not node:
                return
            if node.left is None and node.right is None:
                res[0]+= r*10+node.val
                return

            r=r*10+node.val

            dfs(node.left,r)
            dfs(node.right,r)

        dfs(root,0)
        return res[0]


            
