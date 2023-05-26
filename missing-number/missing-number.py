class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sums=0
        exp = len(nums)
        exp = exp*(exp+1)//2
        for i in nums:
            sums=sums+i
        
        return exp-sums
