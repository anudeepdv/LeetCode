class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n=len(cost)
        dp= [0]*(n+1)

        dp[-1]=0
        dp[n-1]=cost[-1]
        print(dp)
        for i in reversed(range(0,n-1)):
            print(i)
            dp[i]=min(cost[i]+dp[i+1],cost[i]+dp[i+2])

        return min(dp[0],dp[1])