class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [0]*n

        if n<2:
            return nums[0]
        dp[0]=nums[0]
        dp[1]=nums[1]

        for i in range(2,n):
            dp[i]=max(dp[i-2]+nums[i],dp[i-3]+nums[i])

        return max(dp[-1],dp[-2])

        