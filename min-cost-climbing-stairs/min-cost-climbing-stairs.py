class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
    
        dp = [0 for i in range(n+1)]
        dp[n]=0
        dp[n-1]=cost[n-1]

        print(dp)
        for i in reversed(range(0,n-1)):
            dp[i]=min(cost[i]+dp[i+1],cost[i]+dp[i+2])

        print(dp)
        return min(dp[0],dp[1])