class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m=len(grid)
        n=len(grid[0])
        fresh=0
        q=collections.deque()
        visited=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                    visited.add((i,j))

                elif grid[i][j]==1:
                    fresh+=1

        time=1
        if fresh==0:
            return 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:

            for i in range(len(q)):

                ox,oy = q.popleft()

                for x,y in directions:

                    nx,ny = ox+x,oy+y

                    if nx in range(m) and ny in range(n) and grid[nx][ny]==1 and (nx,ny) not in visited:
                        q.append((nx,ny))
                        visited.add((nx,ny))
                        fresh=fresh-1

                        if fresh==0:
                            return time



            time+=1

        return -1




