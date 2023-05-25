# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res = []

        def inOrder(node):

            if node is None:
                return
            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)

        inOrder(root)
        print(res,sorted(res))

        return sorted(set(res))==res