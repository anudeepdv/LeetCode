class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        t = 0 
        b= rows-1

        res=None
        while t<=b:
            m = (t+b)//2
            if target <matrix[m][0]:
                b=m-1
            elif target >matrix[m][-1]:
                t=m+1
            else:
                res=m
                break
        if res is None:
            return False

        l=0
        r=cols-1
        found=None
        while l<=r:
            m = (l+r)//2
            if target >matrix[res][m]:
                l=m+1
            elif target < matrix[res][m]:
                r=m-1
            else:
                found = m
                return True

        return False
        