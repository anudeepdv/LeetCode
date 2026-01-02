class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cd = collections.defaultdict(set)
        rd = collections.defaultdict(set)
        rcd  = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                
                val = board[r][c]
                if val!='.':
                    if val in rd[r] or val in cd[c] or val in rcd[r//3,c//3]:
                        return False
                    else:
                        rd[r].add(val)
                        cd[c].add(val)
                        rcd[r//3,c//3].add(val)

        return True