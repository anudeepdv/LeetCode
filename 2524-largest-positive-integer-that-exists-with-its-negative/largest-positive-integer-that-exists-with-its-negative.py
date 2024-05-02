class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        s = set(nums)

        nums.sort()

        for i in range(len(nums)-1,-1,-1):
            if nums[i]>0:
                if -nums[i] in s:
                    return nums[i]

            else:
                return -1

        return -1

