class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        stick_len = len(cuts)

        dp = [[0]* stick_len for _ in range(stick_len)]

        for i in range(stick_len - 2, -1, -1):
            for j in range(i + 2, stick_len):
                min_cost = float("inf")
                for k in range(i + 1, j):
                    cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                    min_cost = min(min_cost, cost)
                dp[i][j] = min_cost

        return dp[0][stick_len - 1]