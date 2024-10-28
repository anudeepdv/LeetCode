# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([(root,0,0)])

        d = collections.defaultdict(list)
        minx=0
        maxx=0
        while q:
            for _ in range(len(q)):
 
                node,x,y = q.popleft()
               
                minx=min(minx,x)
                maxx=max(maxx,x)
                d[x].append((node.val,-y))
                print(d)

                if node.left:
                    q.append((node.left,x-1,y-1))
                if node.right:
                    q.append((node.right,x+1,y-1))

        print(d)
        res=[]
        for i in range(minx,maxx+1):
            d[i].sort(key = lambda x: (x[1],x[0]))

            r = [d[i][j][0] for j in range(len(d[i]))]
            print(r)
            res.append(r)

        return res
