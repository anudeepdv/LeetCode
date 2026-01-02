class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for i,val in enumerate(nums):
            c=1
            if val - 1 not in nums:
                while val +1 in nums:
                    c+=1
                    val=val+1

            res=max(res,c)
        return res
