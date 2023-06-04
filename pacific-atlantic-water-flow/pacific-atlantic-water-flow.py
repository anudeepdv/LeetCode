class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pac=set()
        atl=set()

        rows=len(heights)
        cols=len(heights[0])


        def bfs(r,c,s):
            q = collections.deque()

            q.append((r,c,heights[r][c]))
            s.add((r,c))

            directions=[[1,0],[0,1],[-1,0],[0,-1]]

            while q:
                x,y,val = q.popleft()
                for i,j in directions:
                    nx,ny = x+i,y+j

                    if nx in range(rows) and ny in range(cols) and heights[nx][ny]>=val and (nx,ny) not in s:
                         q.append((nx,ny,heights[nx][ny]))
                         s.add((nx,ny))


        #first row and last row
        for i in range(cols):
            bfs(0,i,pac)
            bfs(rows-1,i,atl)

        for i in range(rows):
            bfs(i,0,pac)
            bfs(i,cols-1,atl)
        res=[]
        for x,y in pac & atl:
            res.append([x,y])

        return res


