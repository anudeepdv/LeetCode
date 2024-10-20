class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        vis = set()


        def dfs(x,y,vis):

            if x not in range(rows) or y not in range(cols):
                return
            if grid[x][y]=="0":
                return
            if (x,y) in vis:
                return

            vis.add((x,y))

            for xi,yi in dirs:
                dfs(x+xi,y+yi,vis)

        res=0
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in vis and grid[i][j]=="1":
                    res+=1
                    dfs(i,j,vis)

        return res
