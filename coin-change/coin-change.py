class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        dp= [float('inf') for i in range(amount+1)]
        dp[0]=0

        for i in range(1,amount+1):
            for c in coins:
               
                if i-c>=0:
                   
                    dp[i]=min(1+dp[i-c],dp[i])



        return dp[amount] if dp[amount] != float('inf') else -1