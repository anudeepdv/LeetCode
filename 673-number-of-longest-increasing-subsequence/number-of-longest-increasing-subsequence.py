class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        counts = [1] * n
        l=1
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[j]+1> dp[i]:
                        dp[i]=dp[j]+1
                        counts[i]=counts[j]

                    elif dp[j]+1==dp[i]:
                        dp[i]=dp[j]+1
                        counts[i]+=counts[j]

            l=max(l,dp[i])
        res=0
        for d,c in zip(dp,counts):
            if d==l:
                res+=c

        return res

        


        