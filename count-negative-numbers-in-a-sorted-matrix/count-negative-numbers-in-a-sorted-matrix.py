class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        cur=len(grid[0])-1

        res=0

        for row in grid:
            while cur>=0 and row[cur]<0:
                cur=cur-1
            print(cur)
            res = res+(len(row)-cur-1)

        return res