class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [0 for i in range(n)]

        dp[0]=nums[0]

        for i in range(1,n):
            x = 0 if i-2<0 else dp[i-2]
            y = 0 if i-3<0 else dp[i-3]
            dp[i]=max(nums[i]+x,nums[i]+y)

        print(dp)
        return max(dp[n-1],dp[n-2])