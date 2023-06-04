class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows =len(grid)
        cols=len(grid[0])

        fresh=0
        q=collections.deque()
        visited=set()
        initialRotten=0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==1:
                    fresh=fresh+1
                elif grid[r][c]==2:
                    q.append((r,c))
                    visited.add((r,c))
                    initialRotten+=1

        # if initialRotten==0 and fresh==0:
        #     return 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        cal=0
        time=0
        while q and cal!=fresh:


            for i in range(len(q)):
                x,y = q.popleft()

                for l,r in directions:
                    nx,ny= x+l,y+r

                    if nx in range(rows) and ny in range(cols) and grid[nx][ny]==1 and (nx,ny) not in visited :
                        q.append((nx,ny))
                        visited.add((nx,ny))
                        cal=cal+1

            time=time+1

        if cal==fresh:
            return time
        return -1

        





        

