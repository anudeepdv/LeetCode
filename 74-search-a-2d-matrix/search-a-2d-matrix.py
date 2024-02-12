class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        l=0
        r=len(matrix)*len(matrix[0])-1

        while l<=r:

            m = (l+r)//2
            ele = matrix[m//len(matrix[0])][m%len(matrix[0])]
            if target== ele:
                return True

            elif target>ele:
                l=m+1
            else:
                r=m-1

        return False