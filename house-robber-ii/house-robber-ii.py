class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def help(nums):
            n=len(nums)
            if n==0:
                return nums[0]
            dp = [0 for i in range(n)]

            dp[0]=nums[0]

            for i in range(1,n):
                x = 0 if i-2<0 else dp[i-2]
                y = 0 if i-3<0 else dp[i-3]
                dp[i]=max(nums[i]+x,nums[i]+y)

            print(dp)
            return max(dp[n-1],dp[n-2])

        if len(nums)>1 :
            return max(help(nums[1:]),help(nums[:-1])) 
        else :
            return nums[0]