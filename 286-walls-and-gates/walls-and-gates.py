class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols=len(rooms[0])
       
        q=collections.deque()
        visited=set()

        for r in range(rows):
            for c in range(cols):

                if rooms[r][c]==0:
                    q.append((r,c))
                    visited.add((r,c))


        l=1

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:

            for i in range(len(q)):
                x,y=q.popleft()

                for dx,dy in directions:
                    nx,ny= x+dx,y+dy

                    if nx in range(rows) and ny in range(cols) and rooms[nx][ny] ==2147483647 and (nx,ny) not in visited:
                        q.append((nx,ny))
                        visited.add((nx,ny))
                        rooms[nx][ny]=l


            l=l+1

            

