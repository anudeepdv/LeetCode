class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        rows= len(matrix)
        cols = len(matrix[0])
        def check(r,c):

            val = matrix[r][c]

            while r in range(rows) and c in range(cols):
                if val != matrix[r][c]:
                    return False
                r+=1
                c+=1

            return True

        
        for c in range(cols):
            if not check(0,c):
                return False

        for r in range(1,rows):
            if not check(r,0):
                return False

        return True