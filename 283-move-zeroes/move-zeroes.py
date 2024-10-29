class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = 0 
        for l in range(len(nums)):
            if nums[l]:
                nums[l],nums[k]= nums[k],nums[l]
                k+=1