# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        q = collections.deque([root])
        res=0

        while q:

            
            for i in range(len(q)):
                r = q.popleft()
                left = r.left
                right = r.right

               

                if left is not None:
                    q.append(left)

                if right is not None:
                    q.append(right)

                
            
            res = res+1

        return res