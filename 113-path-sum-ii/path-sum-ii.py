# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res=[]
        def dfs(node,l):

            if not node:
                return
            print(l)
            if node.left is None and node.right is None:
                l.append(node.val)
                if sum(l)==targetSum:
                    res.append([i for i in l])

                return

           

            dfs(node.left,l+[node.val])
            dfs(node.right,l+[node.val])

        dfs(root,[])
        return res
            