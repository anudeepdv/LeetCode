class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows= len(maze)
        cols=len(maze[0])
        

        dir= [(0,1),(1,0),(-1,0),(0,-1)]

        vis=set()

        def dfs(x,y,vis):

            if x not in range(rows) or y not in range(cols):
                return False

            if (x,y) in vis:
                return False

            if x==destination[0] and y==destination[1]:
                return True

            vis.add((x,y))

            ret=False

            for i,j in dir:

                nx,ny = x,y

                while nx+i in range(rows) and ny+j in range(cols) and maze[nx+i][ny+j]==0:
                    nx=nx+i
                    ny=ny+j
                
                ret = ret or dfs(nx,ny,vis)

            return ret

        return dfs(start[0],start[1],vis)

        

                