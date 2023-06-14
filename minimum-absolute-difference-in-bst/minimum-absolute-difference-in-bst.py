# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        q= collections.deque()
        visited=set()

        q.append((root,-1))
        visited.add(root)
        res= float('inf')
        trav=[root.val]
        while q:

            

            for  i in range(len(q)):

                n,rt = q.popleft()

                if n.left:
                    l=n.left
                    trav.append(l.val)
                    res=min(res,abs(n.val-l.val))
                    q.append((l,n))
                    visited.add(l)

                if n.right:
                    r=n.right
                    trav.append(r.val)
                    res=min(res,abs(r.val-n.val))
                    q.append((r,n))
                    visited.add(r)

        trav.sort()
        for i in range(1,len(trav)):
            res=min(res,trav[i]-trav[i-1])
        return res




