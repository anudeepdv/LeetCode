class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        dp= [-1 for i in range(amount+1)]

        dp[0]=0

        for i in range(n):
            for j in range(0,amount+1):

                if j-coins[i]>=0:
                    if dp[j-coins[i]]!=-1:
                        if dp[j]!=-1:

                            dp[j]=min(dp[j],1+dp[j-coins[i]])
                        else:
                            dp[j]=1+dp[j-coins[i]]
        print(dp[-1])

        return dp[-1]

                