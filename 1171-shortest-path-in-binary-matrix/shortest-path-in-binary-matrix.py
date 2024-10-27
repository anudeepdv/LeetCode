class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        q = collections.deque()
        vis = set()

        if grid[0][0]==0:
            q.append((0,0,1))
            vis.add((0,0))

        dirs = [(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
    
        n = len(grid)
        while q:
            x,y,r = q.popleft()

            if x==n-1 and y==n-1:
                return r

            for i,j in dirs:
                nx,ny = x+i,y+j
                if nx in range(n) and ny in range(n) and grid[nx][ny]==0 and (nx,ny) not in vis:
                    q.append((nx,ny,r+1))
                    vis.add((nx,ny))

        return -1