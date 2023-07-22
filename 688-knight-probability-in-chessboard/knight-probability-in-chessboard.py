class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        d = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2))

        q={(row,column):1}
        f=k
        while q and k>0:

            tempq=collections.defaultdict(int)

            for cx,cy in q:
                print(cx,cy)
                for x,y in d:
                    nx,ny =x+cx,y+cy

                    if nx in range(n) and ny in range(n):
                        tempq[(nx,ny)]+=q[(cx,cy)]

            q=tempq
            k-=1

        return sum(q.values())/ (8**f)

        


    