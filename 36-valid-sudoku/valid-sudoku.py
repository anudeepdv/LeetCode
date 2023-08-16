class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        r=collections.defaultdict(set)
        c=collections.defaultdict(set)
        b=collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]=='.':
                    continue
                else:
                    if  board[i][j] in r[i] or board[i][j] in c[j] or board[i][j] in b[(i//3,j//3)]:
                        return False
                    
                    else: 
                        r[i].add(board[i][j])
                        c[j].add(board[i][j])
                        b[(i//3,j//3)].add(board[i][j])


        return True