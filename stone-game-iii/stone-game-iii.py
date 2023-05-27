class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0 for _ in range(len(stoneValue))]
        if len(dp) >= 1:
            dp[-1] = stoneValue[-1]
        if len(dp) >= 2:
            dp[-2] = max(stoneValue[-1] + stoneValue[-2], stoneValue[-2] - dp[-1])
        if len(dp) >= 3:
            dp[-3] = max(stoneValue[-3] + stoneValue[-1] + stoneValue[-2], stoneValue[-3] - dp[-2], stoneValue[-3] + stoneValue[-2] - dp[-1])
        
        for i in range(len(stoneValue) - 4, -1, -1):
            
            dp[i] = max([sum(stoneValue[i: i + j]) - dp[i + j] for j in range(1, 4)])
        
        if dp[0] > 0:
            return "Alice"
        if dp[0] == 0:
            return "Tie"
        return "Bob"