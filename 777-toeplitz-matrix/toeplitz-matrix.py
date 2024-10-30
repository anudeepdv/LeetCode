class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])
        def check(r,c):

            val = matrix[r][c]

            while r in range(rows) and c in range(cols):

                if matrix[r][c]!=val:
                    return False

                r+=1
                c+=1

            return True

        
        for i in range(0,cols):
            if not check(0,i):
                return False

        for i in range(1,rows):
            if not check(i,0):
                return False

        return True
