class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        index= -1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                index=i

        if index==-1:
            nums.reverse()
            return

        peak = nums[index]
        peaki = index

        for i in range(peaki, len(nums)):
            if nums[i]>nums[index-1] and nums[i]<peak:
                peak = nums[i]
                peaki = i
        print(peaki,index-1)
        nums[peaki],nums[index-1] =nums[index-1] , nums[peaki]
        nums[index:] = sorted(nums[index:])


        

        
