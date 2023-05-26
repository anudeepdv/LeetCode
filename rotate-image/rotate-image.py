class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l , r = 0 , len(matrix)-1

        while (l<r):

            for i in range(r-l):
                t,b=l,r
                temp = matrix[t][l+i]
                #bottum left to top left
                matrix[t][l+i]=matrix[b-i][l]

                #bottom right to bottom left
                matrix[b-i][l]=matrix[b][r-i]

                # top right to bottom right
                matrix[b][r-i]=matrix[t+i][r]

                matrix[t+i][r]= temp
            l=l+1
            r=r-1

    
