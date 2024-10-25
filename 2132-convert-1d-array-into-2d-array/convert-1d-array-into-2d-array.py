class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        res = [[0]*n for _ in range(m)]

        if m * n != len(original):
            return []
        for i in range(len(original)):
            val = original[i]

            row = i//n
            col=i%n
            print(row,col)
            res[row][col] = val

        return res
