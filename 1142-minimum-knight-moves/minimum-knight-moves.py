class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:


        dir = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        q=collections.deque()

        q.append((0,0))

        vis=set()
        vis.add((0,0))
        res=0
        while q:
            for _ in range(len(q)):
                
                x1,y1 = q.popleft()

                if x1==x and y==y1:
                    return res

                for dx,dy in dir:
                    nx,ny = x1+dx,y1+dy

                    if (nx,ny) not in vis:
                        q.append((nx,ny))
                        vis.add((nx,ny))

            res+=1

        

