class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        n = len(grid)

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        visited=set()

        def invalid(r,c):
            return r<0 or c<0 or r==n or c==n
               

        def dfs(r,c):

            if invalid(r,c)or  not grid[r][c] or (r,c) in visited  :
                return 
            
            visited.add((r,c))

            for a,b in directions:
                newl, newr = r+a,c+b
                dfs(newl,newr)


        def bfs():
            
            res , q =0 , collections.deque(visited)

            while q:

                for i in range(len(q)):
                    r,c = q.popleft()

                    for a,b in directions:
                        newx,newy = r+a,c+b
                        if(invalid(newx,newy) or (newx,newy) in visited):
                            continue
                        if grid[newx][newy]:
                            return res   
                        q.append([newx,newy]) 
                        visited.add((newx,newy))

                res=res+1   




        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c]:
                    dfs(r,c)

                    print(visited)
                    return bfs()
                
                
        
