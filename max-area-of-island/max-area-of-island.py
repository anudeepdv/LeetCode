class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited=set()
        res=0

        def bfs(r,c):

            cur=1
            q= collections.deque()
            q.append((r,c))
            visited.add((r,c))

            dir = [[0,1],[1,0],[-1,0],[0,-1]]

            while q:
                x,y=q.popleft()

                for dx,dy in dir:
                    nx,ny = x+dx, y+dy

                    if nx in range(rows) and ny in range(cols) and grid[nx][ny]==1 and (nx,ny) not in visited:
                        q.append((nx,ny))
                        visited.add((nx,ny))
                        cur=cur+1

            return cur




        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==1 and (r,c) not in visited:

                    l =bfs(r,c)
                    res=max(res,l)


        return res