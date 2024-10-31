class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        island_id=-1
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        area_map = collections.defaultdict(int)
        
        def dfs(x,y):
            if x not in range(rows) or y not in range(cols):
                return

            if grid[x][y]!=1:
                return

            
            grid[x][y] = island_id
            area_map[island_id]+=1
            for i, j in dir:
                nx,ny = x+i,y+j
                dfs(nx,ny)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    dfs(r,c)
                    island_id-=1

        print(grid)

        max_area=0
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c]==0:
                    area=1
                    sur_set=set()

                    for x,y in dir:
                        nx,ny = r+x,c+y
                        if nx in range(rows) and ny in range(cols):
                            sur_set.add(grid[nx][ny])
                    for id in sur_set:
                        area+=area_map[id]

                    max_area = max(max_area,area)


        return max_area if max_area!=0 else rows*cols




       

        


