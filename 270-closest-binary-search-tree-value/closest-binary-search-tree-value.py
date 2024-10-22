# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        res=math.inf
        mindis = math.inf

        def dfs(node):
            nonlocal res
            nonlocal mindis
            
            if not node:
                return

            if abs(node.val-target)<mindis:
                res=node.val
                mindis = abs(node.val-target)
            elif abs(node.val-target) == mindis:
                res=min(res,node.val)

            if target>node.val:
                dfs(node.right)
            elif target<node.val:
                dfs(node.left)

                


        dfs(root)
        return res
