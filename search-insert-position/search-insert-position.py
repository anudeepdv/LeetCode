class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l=0
        r=len(nums)-1
        res=0

        if target > nums[-1]:
            return len(nums)
        while l<=r:

            m=(l+r)//2

            if target<=nums[m]:
                res=m
                r=m-1
            else:
                l=m+1

        return res