class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        vis = set()

        q= collections.deque()

        def dfs(x,y,vis):

            if not ( x in range(rows) and y in range(cols) and grid[x][y]=="1"):
                return
            if (x,y) in vis:
                return

            vis.add((x,y))
            for xi , xj in dirs:
                dfs(x+xi, y+xj, vis)


        res=0
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1" and (i,j) not in vis:
                    dfs(i,j,vis)
                    res+=1
        return res