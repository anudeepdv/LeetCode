class Solution:
    def fib(self, n: int) -> int:

        if n<2:
            return n
        dp =[0 for i in range(n+1)]
        dp[1]=1
        for i in range(2,n+1):
            print(dp)
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]
