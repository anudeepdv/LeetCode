class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows= len(board)
        cols=len(board[0])
        copyBoard = [ [board[r][c] for c in range(cols)] for r in range(rows)]

        nei = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]

        for r in range(rows):
            for c in range(cols):
                living=0
                dead=0
                for x,y in nei:
                    if r+x in range(rows) and c+y in range(cols):
                        if copyBoard[ r+x][c+y]==1:
                            living+=1
                        else:
                            dead+=1
                print(living,dead)
                if copyBoard[r][c]==1:

                    if living<2 or living>3:
                        board[r][c]=0
                    elif living==2 or living==3:
                        board[r][c]=1
                else:
                    if living==3:
                        board[r][c]=1


