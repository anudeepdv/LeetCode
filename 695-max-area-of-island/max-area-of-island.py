class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m= len(grid)
        n=len(grid[0])

        vis=set()
        res=0

        def bfs(x,y):

            q=collections.deque()
            q.append((x,y))
            vis.add((x,y))
            dirs=[[1,0],[0,1],[-1,0],[0,-1]]
            c=1
            while q:

                xi,xj = q.popleft()

                for ci,cj in dirs:
                    nx,ny = xi+ci,xj+cj

                    if nx in range(m) and ny in range(n) and (nx,ny) not in vis and grid[nx][ny]==1:
                        q.append((nx,ny))
                        vis.add((nx,ny))
                        c+=1

            return c







        for i in range(m):
            for j in range(n):

                if (i,j) not in vis and grid[i][j]==1:
                    s=bfs(i,j)

                    res=max(res,s)

        return res

