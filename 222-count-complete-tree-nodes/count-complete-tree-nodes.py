# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    


    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        def getl(n):
            d=1
            while n.left:
                d=d+1
                n=n.left
            return d

        def getr(n):
            d=1
            while n.right:
                d=d+1
                n=n.right
            return d
        ld = getl(root)
        rd = getr(root)

        if ld==rd:
            return 2**ld -1

        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right) 

            
