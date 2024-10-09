# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        if not root:
            return []
        l =True

        q = collections.deque([root])

        res= []
        while q:


            if l:
                temp = [i.val for i in q]
                res.append(temp)
                l=False
            else:
                temp = [i.val for i in reversed(q)]
                res.append(temp)
                l=True

            for _ in range(len(q)):

                pop = q.popleft()

                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)

        return res
