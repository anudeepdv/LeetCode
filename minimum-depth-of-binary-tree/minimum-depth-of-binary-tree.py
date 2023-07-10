# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        q=collections.deque()
        if root is None:
            return 0
        q.append((root,1))
        
        res=float('inf')
        while q:
            for _ in range(len(q)):
                pop,d = q.popleft()

                if pop.left is None and pop.right is None:
                    res=min(res,d)
                
                if pop.left:
                    q.append((pop.left,d+1))
                if pop.right:
                    q.append((pop.right,d+1))

        return res
