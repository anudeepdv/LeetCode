class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        curSum=0
        maxSum=0

        for i in gain:
            print(curSum,i)
            curSum=curSum+i
            
            if curSum>maxSum:
                maxSum=curSum

        return maxSum
