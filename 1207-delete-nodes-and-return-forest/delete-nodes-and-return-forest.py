# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        output=set()
        output.add(root)
        delete=set(to_delete)

        def dfs(node):

            if not node:
                return

            res=node
            if node.val in delete:
                res=None
                output.discard(node)
                if node.left:
                    output.add(node.left)
                if node.right:
                    output.add(node.right)


            node.left = dfs(node.left)
            node.right=dfs(node.right)

            return res


        dfs(root)

        return list(output)
