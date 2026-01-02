class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l1 = [1 for i in range(len(nums))]
        l2 = [1 for i in range(len(nums))]

        for i in range(1,len(nums)):
            l1[i]=l1[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
           
            l2[i]=l2[i+1]*nums[i+1]

        for i in range(len(nums)):
            l1[i]=l1[i]*l2[i]

        return l1

    
        