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
            popx, popy = q.popleft()

            if popx == destination[0] and popy==destination[1]:
                return True


            for ix,iy in dir:

                nx,ny = popx+ix, popy+iy

                while nx in range(rows) and ny in range(cols)  and maze[nx][ny]==0:
                    nx=nx+ix
                    ny=ny+iy

                nx=nx-ix
                ny=ny-iy

                if (nx,ny) not in vis and maze[nx][ny]==0:
                    q.append((nx,ny))
                    vis.add((nx,ny))

        return False