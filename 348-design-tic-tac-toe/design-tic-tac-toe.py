class TicTacToe:

    def __init__(self, n: int):
        self.rd = [0]*n
        self.cd =[0]*n
        self.c1=0
        self.c2=0
        self.n=n
        

    def move(self, row: int, col: int, player: int) -> int:

        val = -1 if player ==1 else 1

        self.rd[row]+=val
        self.cd[col]+=val

        if row==col:
            self.c1+=val
        if row+col==self.n-1:
            self.c2+=val

        if max(abs(self.rd[row]),abs(self.cd[col]),abs(self.c1),abs(self.c2))==self.n:
            return player
        
        return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)