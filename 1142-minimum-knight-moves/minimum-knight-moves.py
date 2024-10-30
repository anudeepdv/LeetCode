class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:


        dir = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        q = deque()
        q.append((0,0,0))
        vis=set()
        vis.add((0,0))

        while q:

            i,j,r = q.popleft()

            if i==x and j==y:
                return r
            
            for ix,ij in dir:
                nx,ny = i+ix,j+ij
                if (nx,ny) not in vis:
                    q.append((nx,ny,r+1))
                    vis.add((nx,ny))

            