# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        q=collections.deque()
        if root is None:
            return False
        q.append((root,root.val))

        while q:
            
            for _ in range(len(q)):
                node,val=q.popleft()
                print(node.val,val)
                if node.left is None and node.right is None and val==targetSum:
                    return True
                if  node.left:
                    q.append((node.left,val+node.left.val))
                if  node.right:
                    q.append((node.right,val+node.right.val))



                


        return False
