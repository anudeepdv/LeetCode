class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()
        l = nums[0]
        r = len(nums)-1
        res=0
        for i in range(len(nums)):
            while nums[i]+nums[r]>target and i<=r:
                r=r-1
            
            if( i<=r):
                res = res+ (2**(r-i))

        res=res%(10**9 +7)
        return res
            
