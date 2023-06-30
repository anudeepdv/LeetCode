class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        grid = [ [ 0 for i in range(col)] for j in range(row)]
 
        
        

        l=0

        r=len(cells)-1
        res=0

        def bfs(mid):
            q = collections.deque()
            visited=set()

            mat =[ [ 0 for i in range(col)] for j in range(row)]
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            # print(mid)
            # print(mat,grid)
            for i in range(mid):
                a,b =cells[i]
                mat[a-1][b-1]=1

            # print(mat)

            end =set()
            for i in range(0,col):
                if mat[0][i]==0:
                    q.append((0,i))
                    visited.add((0,i))

                if mat[row-1][i]==0:
                    end.add((row-1,i))

            # print(visited)
            # print(end)

            while q:

                for i in range(len(q)):

                    x,y = q.popleft()

                    if (x,y) in end:
                        return True
                    
                    for a,b in directions:
                        nx = a+x
                        ny=b+y

                        if nx in range(row) and ny in range(col) and mat[nx][ny]==0 and (nx,ny) not in visited:
                            q.append((nx,ny))
                            visited.add((nx,ny))
            return False


        while l<=r:
            m=(l+r)//2
            
            if(bfs(m)):
                res=m
                l=m+1
            else:
                r=m-1

        return res


