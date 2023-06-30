class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        curMax = arrays[0][-1]
        curMin = arrays[0][0]

        res=-float('inf')
        for i in range(1,len(arrays)):

            mi=arrays[i][0]
            ma=arrays[i][-1]

            res = max(res, abs(ma-curMin))
            res = max(res, abs(curMax-mi))

            curMin=min(curMin,mi)
            curMax=max(curMax,ma)

        return res

