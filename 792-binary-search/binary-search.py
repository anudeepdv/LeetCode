class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
      

        l=0 
        r=len(nums)-1

        while l<=r:

            m=(l+r)//2

            if nums[m]==target:
                return m
            elif target>nums[m]:
                l=m+1
            else:
                r=r-1

        return -1