class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l=0
        r= len(matrix)*len(matrix[0])-1

        while l<=r:
            m = (l+r)//2

            val = matrix[m//len(matrix[0])][m%len(matrix[0])]
            print(val)
            if val==target:
                return True
            if val>target:
                r=m-1
            else:
                l=m+1
        return False
            
            