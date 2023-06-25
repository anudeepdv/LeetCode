class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}  

        for rod in rods:
            # Create a shallow copy of current dp table
            # to avoid modifying it while iterating over it
            curr_dp = dp.copy()

            for height in curr_dp:
                dp[height + rod] = max(dp.get(height + rod, 0), curr_dp[height])
            
                dp[abs(height - rod)] = max(dp.get(abs(height - rod), 0), curr_dp[height] + min(height, rod))

        return dp.get(0, 0)  