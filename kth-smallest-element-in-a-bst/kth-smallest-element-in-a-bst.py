# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        s=[]

        def inOrder(r):
            if r is None:
                return
            inOrder(r.left)
            s.append(r.val)
            inOrder(r.right)
        inOrder(root)
        print(s)
        return s[k-1]


