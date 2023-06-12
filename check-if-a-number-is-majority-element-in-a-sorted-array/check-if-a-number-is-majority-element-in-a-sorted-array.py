class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        l=0
        n=len(nums)
        r = n-1
        i=0
        while (l<=r):

            m = (l+r)//2

            if target<=nums[m]:
                r=m-1
                i=m
            else:
                l=m+1

       
        if i+n//2 <n and nums[i+n//2]==target:
            return True
        return False