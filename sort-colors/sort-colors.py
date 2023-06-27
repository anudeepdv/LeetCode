class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l=0
        r=len(nums)-1
        i=0

        def swap(a,b):
            temp=nums[a]
            nums[a]=nums[b]
            nums[b]=temp
        while i<=r:

            if nums[i]==2:
                
                swap(i,r)
                r=r-1
                i=i-1
            elif nums[i]==0:
                # nums[i],nums[l]=nums[l],nums[i]
                swap(i,l)
                l=l+1
            i=i+1