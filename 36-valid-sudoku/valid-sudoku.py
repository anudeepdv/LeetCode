class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for rowno in range(len(board)):
            for colno in range(len(board[0])):
                
                
                val = board[rowno][colno] 
                if val =='.':
                    continue
                if val in row[rowno] or val in cols[colno] or val in box[(rowno//3,colno//3)]:
                    return False
                
                row[rowno].add(val)
                cols[colno] .add(val)
                box[(rowno//3,colno//3)].add(val)


        return True