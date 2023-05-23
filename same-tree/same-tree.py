# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def isEquals(tree1,tree2):

            if tree1 is None and tree2 is not None:
                return False

            if tree2 is None and tree1 is not None:
                return False

            if tree1 is None and tree2 is None:
                return True
            
            if tree1.val == tree2.val:
                return isEquals(tree1.left,tree2.left) and isEquals(tree1.right,tree2.right)
            else:
                return False

        return isEquals(p,q)
