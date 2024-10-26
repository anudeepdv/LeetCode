class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        building=1
        obstacle =2
        empty=0

        dist_matrix = [[0]*cols for i in range(rows)]

        dirs = [(0,-1),(-1,0),(1,0),(0,1)]

        best = -1

        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==building:
                    localdist = float('infinity')
                    q = deque()
                    q.append((r,c,0))

                    while q:
                        x,y,d = q.popleft()
                        for i, j in dirs:
                            nx,ny = x+i,y+j

                            if nx in range(rows) and ny in range(cols) and grid[nx][ny]==empty:
                                grid[nx][ny]-=1
                                dist_matrix[nx][ny]+=d+1
                                q.append((nx,ny,d+1))
                                localdist=min(localdist,dist_matrix[nx][ny])

                    empty-=1
                    best=localdist


        return best if best!=float('infinity') else -1


                        
