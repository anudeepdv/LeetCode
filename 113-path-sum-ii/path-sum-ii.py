# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res=[]
        def dfs(node,s):
            if not node:
                return

            
            print(s)
            if not node.left and not node.right and sum(s)+node.val==targetSum:
                res.append(s+[node.val])
                return

            dfs(node.left,s+[node.val])
            dfs(node.right,s+[node.val])

            return

        dfs(root,[])
        return res