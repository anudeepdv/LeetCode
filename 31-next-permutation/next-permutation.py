class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        index =-1

        for i in range(1,len(nums)):

            if nums[i]>nums[i-1]:
                index =i

        if index ==-1:
            print("k")
            nums.reverse()
            return        
        peak = nums[index]
        peaki = index
        prev = nums[index-1]
        print(prev,"PPREC")
        print(peak,peaki,"PEK")
        for i in range(peaki+1,len(nums)):
            if nums[i]>prev and nums[i]<=peak:
                peaki = i 
                peak = nums[i]
                print(peak, "peak")
        nums[peaki] ,nums[index-1] = nums[index-1], nums[peaki]
        nums[index:]=reversed(nums[index:])
