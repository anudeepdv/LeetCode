# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        #Time complex =O(N) Space O(N)
        q= deque()
        q.append(root)

        nullnode= False

        while q:

            node = q.popleft()

            if not node:
                nullnode=True
            else:
                if nullnode:
                    return False
                
                q.append(node.left)
                q.append(node.right)

        return True
           