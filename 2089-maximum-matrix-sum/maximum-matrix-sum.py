class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        negativeCount = 0
        minabs = float("inf")
        res=0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                val = matrix[r][c]
                res+=abs(val)
                if val<0:
                    negativeCount+=1
                minabs = min(minabs,abs(val))
        if negativeCount%2==0:
            return res
        return res-2*(minabs)