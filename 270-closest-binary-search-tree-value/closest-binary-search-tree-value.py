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
            print(node.val)
            if abs(node.val-target)<mindis:
                res=node.val
                mindis = abs(node.val-target)
            if abs(node.val-target)==mindis:
                res=min(node.val,res)

            if target>node.val:
                dfs(node.right)
            else:
                dfs(node.left)

        dfs(root)
        return res
