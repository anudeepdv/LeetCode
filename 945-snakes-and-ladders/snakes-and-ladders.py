class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        board.reverse()
        rows = len(board)
        cols=rows
        q= collections.deque([(1,0)])
        n=rows*rows
        vis = set()
        vis.add(1)
        def getpos(pos):
            rowno = (pos-1)//rows
            colno = (pos-1)%rows
            if rowno%2:
                colno = rows-1-colno

            return rowno,colno

        while q:
            
            pos , move = q.popleft()
            

            for i in range(1,7):
                newpos = pos+i
               
                r,c = getpos(newpos)

                if board[r][c]!=-1:
                    newpos = board[r][c]
                    r,c = getpos(newpos)

                if newpos==n:
                    return move+1
                
                if newpos not in vis:
                    q.append((newpos,move+1))
                    vis.add(newpos)


        return -1
