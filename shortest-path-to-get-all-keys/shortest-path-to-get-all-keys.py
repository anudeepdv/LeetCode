import collections

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        #1 . find the start point
        #2. find how many key we need to collection
        cnt = 0
        start=None
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    start = [r,c]
                if grid[r][c] in 'abcdef':
                    cnt += 1

        q= collections.deque()
        visited=set()

        q.append((start[0],start[1],''))

        directions=[[-1,0],[0,1],[1,0],[0,-1]]
        steps=0
        while q:

            for _ in range(len(q)):

                r,c,keys=q.popleft()

                if (r,c,keys) in visited:
                    continue

                if len(keys)==cnt:
                    return steps

                visited.add((r,c,keys))

                for nx,ny in directions:
                    x=r+nx
                    y=c+ny
                    if x in range(rows) and y in range(cols) and grid[x][y] !='#':
                        if grid[x][y] in '.@':
                            q.append((x,y,keys))
                        if  grid[x][y] in "abcdef" and grid[x][y] not in keys:
                            q.append((x,y,keys+grid[x][y]))
                        if  grid[x][y] in "abcdef" and grid[x][y]  in keys:
                            q.append((x,y,keys))
                        if grid[x][y] in "ABCDEF" and grid[x][y].lower() in keys:
                            q.append((x,y,keys))

                        


            steps = steps+1


        return -1




            


      