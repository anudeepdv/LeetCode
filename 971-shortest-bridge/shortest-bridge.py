class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        rows  = len(grid)
        cols = len(grid[0])

        def dfs(i,j,vis):
            if i not in range(rows) or j not in range(cols):
                return
            if (i,j) in vis:
                return 
            if grid[i][j] !=1:
                return
            
            vis.add((i,j))

            dfs(i+1,j,vis)
            dfs(i,j+1,vis)
            dfs(i-1,j,vis)
            dfs(i,j-1,vis)

        visa=set()  
        visb=set() 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and not visa:
                    dfs(r,c,visa)
                elif  grid[r][c]==1 and (r,c) not in visa and not visb:
                    print(r,c)
                    dfs(r,c,visb)

        print(visa,visb)

        q= collections.deque()
        vis=set()
        for i in visa:
            q.append((i[0],i[1],-1))
            vis.add(i)

        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        while q:

            r,c,l = q.popleft()

            if (r,c) in visb:
                return l

            for x,y in dirs:
                nx,ny = x+r,y+c
                if (nx,ny) not in vis:
                    vis.add((nx,ny))
                    q.append((nx,ny,l+1))

            




