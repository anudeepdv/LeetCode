class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        rows= len(grid)
        columns=len(grid[0])

        res=0

        visited=set()

        def bfs(r,c):
            q= collections.deque()
            q.append((r,c))
            visited.add((r,c))

            directions =[[0,1],[1,0],[-1,0],[0,-1]]

            while q:
                # print(visited)
    
                a,b = q.popleft()

                for x,y in directions:
                    
                    nx,ny = a+x, b+y
                    # print(nx,ny)
                    if nx in range(rows ) and ny in range(columns) and grid[nx][ny]=="1" and (nx,ny )not in visited:
                        q.append((nx,ny))
                        visited.add((nx,ny))


            return

        for r in range(rows):
            for c in range(columns):

                if grid[r][c]=="1" and (r,c) not in visited:
                    # print('hii')
                    bfs(r,c)
                    # print(r,c)
                    # print(visited)
                    res=res+1


        return res