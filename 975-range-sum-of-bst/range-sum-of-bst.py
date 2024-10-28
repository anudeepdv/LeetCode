# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        res = [0]

        def dfs(node):
            if not node:
                return

            if node.val in range(low,high+1):
                res[0]+=node.val
                dfs(node.right)
                dfs(node.left)

            elif node.val<low:
                dfs(node.right)
            else:
                dfs(node.left)

        dfs(root)
        return res[0]

