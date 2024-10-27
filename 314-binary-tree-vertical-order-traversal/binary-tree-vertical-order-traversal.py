# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = collections.deque()
    

        q.append((root,0,0))

        d=collections.defaultdict(list)
        minx= +math.inf
        maxx = -math.inf
        
        while q:
            node,x,y = q.popleft()
            d[x].append(node.val)
            minx=min(minx,x)
            maxx = max(maxx,x)

            if node.left:
                q.append((node.left,x-1,y-1))
            if node.right:
                q.append((node.right,x+1,y-1))


        res=[]

        for i in range(minx,maxx+1):
            res.append(d[i])

        return res

        