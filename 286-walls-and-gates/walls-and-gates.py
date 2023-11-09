class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        vis=set()
        m=len(rooms)
        n=len(rooms[0])
        res=[]
        q=collections.deque()
        dirt=[[0,1],[1,0],[-1,0],[0,-1]]
        r=0
        
        for i in range(m): 
            for j in range(n):
                if rooms[i][j]==0:
                    q.append((i,j))

        c=1
        while q:

            for _ in range(len(q)):

                x,y = q.popleft()

                for i,j in dirt:
                    nx,ny=x+i,y+j
                    
                    if nx in range(m) and ny in range(n) and (nx,ny) not in vis and rooms[nx][ny]==2147483647:
                        q.append((nx,ny))
                        vis.add((nx,ny))
                        rooms[nx][ny]=c

            c+=1

          




