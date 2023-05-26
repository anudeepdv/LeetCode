class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n =len(matrix)

        m=len(matrix[0])

        row0=1
        for r in range(n):
            for c in range(m):

                if matrix[r][c] ==0 :
                    matrix[0][c]=0

                    if r==0:
                        row0=0
                    else:
                        matrix[r][0]=0

        print(matrix)

        for r in range(1,n):
            for c in range(1,m):


                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0

            
        if matrix[0][0]==0:
            for i in range(n):
                matrix[i][0]=0

        if row0==0:
            for i in range(m):
                matrix[0][i]=0




