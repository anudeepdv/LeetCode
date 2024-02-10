class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows= len(maze)
        cols=len(maze[0])
        q = collections.deque()
        vis=set()

        q.append((start[0],start[1]))
        vis.add((start[0],start[1]))

        dir= [(0,1),(1,0),(-1,0),(0,-1)]

        while q:

            popx,popy = q.popleft()

            if popx==destination[0] and popy==destination[1]:
                return True
            
            for dx,dy in dir:
                nx = popx+dx
                ny = popy+dy

                while nx in range(0,rows) and ny in range(0,cols) and maze[nx][ny]==0:
                    nx=nx+dx
                    ny=ny+dy
                

                nx=nx-dx
                ny=ny-dy

                if (nx,ny) not in vis:
                    vis.add((nx,ny))
                    q.append((nx,ny))


        return False
