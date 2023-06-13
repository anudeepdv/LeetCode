class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        d=collections.defaultdict(int)

        for i in grid:

            d[tuple(i)]= d[tuple(i)]+1

        n=len(grid)
        cnt=0
        for i in range(n):
            c=[]
            for j in range(n):
                c.append(grid[j][i])
            c=tuple(c)
            if c in d:

                cnt=cnt+d[c]
            c=[]

        return cnt
