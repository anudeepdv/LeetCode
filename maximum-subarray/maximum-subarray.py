class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr =nums[0]
        maxx =nums[0]
     
        for i in nums[1:]:
            curr = max(i,curr+i)
            maxx = max(curr,maxx)

        return maxx