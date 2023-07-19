# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        

        res=float('inf')
        val=[]
        q=collections.deque()
        q.append(root)

        while q:
            for _ in range(len(q)):
                pop = q.popleft()
                print(pop.val,abs(pop.val-target),target,res)
                if abs(pop.val-target)<res:
                    res=abs(pop.val-target)
                    val=pop.val
                if abs(pop.val-target)==res:
                    val=min(pop.val,val)

                if pop.left:
                    q.append(pop.left)

                if pop.right:
                    q.append(pop.right)
        print(val)
        return val
