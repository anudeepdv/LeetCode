class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(x,y,k,vis):

            if k ==len(word):
                return True
            if x not in range(len(board)) or y not in range(len(board[0])) or board[x][y]!=word[k] or (x,y) in vis:
                return False
            vis.add((x,y))

            r = (dfs(x-1,y,k+1,vis) or
            dfs(x,y-1,k+1,vis)or
            dfs(x+1,y,k+1,vis) or
            dfs(x,y+1,k+1,vis))

            vis.remove((x,y))
            return r


        for i in range(len(board)):
            for j in range(len(board[0])):

                if dfs(i,j,0,set()):
                    return True
        return False