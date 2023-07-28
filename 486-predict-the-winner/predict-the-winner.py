class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        dp = [[[0,0] for i in range(len(nums))] for j in range(len(nums))]

        print(dp)

        for i in range(len(nums)):
            dp[i][i] = [nums[i],0]
        

        for l in range(2,len(nums)+1):
            for i in range(0,len(nums)-l+1):
                j = i+l-1

                if nums[i] + dp[i+1][j][1] > nums[j] + dp[i][j-1][1]:
                    dp[i][j][0] = nums[i] + dp[i+1][j][1]
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = nums[j] + dp[i][j-1][1]
                    dp[i][j][1] = dp[i][j-1][0]

       

                
        print(dp)
        return dp[0][-1][0]>=dp[0][-1][1]
        
        