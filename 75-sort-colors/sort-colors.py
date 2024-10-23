class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l =0 
        m=0 
        r= len(nums)-1

        def swap(a,b):
            temp=nums[a]
            nums[a]=nums[b]
            nums[b]=temp

        while m<=r:

            if nums[m]==2:
                swap(m,r)
                r-=1
            elif nums[m]==0:
                # nums[l],nums[m]=nums[m],nums[l]
                swap(m,l)
                l+=1
                m+=1
            else:
                m+=1

        