# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        res=float('inf')
        q=collections.deque()
        q.append(root)

        h=[]
        while q:
            for _ in range(len(q)):
                pop = q.popleft()
                print(pop.val,abs(pop.val-target),target,res)
                h.append((abs(pop.val-target),pop.val))
             

                if pop.left:
                    q.append(pop.left)

                if pop.right:
                    q.append(pop.right)
       
       
        heapq.heapify(h)
        r=[]

        for i in range(k):
            r.append(heapq.heappop(h)[1])

        return r