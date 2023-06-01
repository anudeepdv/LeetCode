class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n=len(grid)
        if grid[0][0]==1:
            return -1

        q =collections.deque()
        q.append([0,0,0])

        direction = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
        while q:
            print(q)
            for i in range(len(q)):
                rcl=q.popleft()
                row,col,l =rcl[0],rcl[1],rcl[2]
                if row==n-1 and col==n-1:
                    return l+1
                
                else :
                    for d in direction:
                        newr =  row+d[0]
                        newc = col+d[1]

                        if newc >=0 and newc <n and newr >=0 and newr <n and grid[newr][newc]==0:
                            q.append([newr,newc,l+1])
                            grid[newr][newc]=1

        return -1
