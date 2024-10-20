# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])

        res=[]
        while q:
            res.append(q[-1].val)
            for _ in range(len(q)):
                pop = q.popleft()

                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)

        return res