class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        res=[]

        if not nums:
            return [[lower,upper]]

        if lower!=nums[0]:
            res.append([lower,nums[0]-1])
        
        prev= nums[0]

        for i in range(1,len(nums)):
            if nums[i]!=prev+1:
                res.append([prev+1,nums[i]-1])
            prev=nums[i]

        if prev!=upper:
            res.append([prev+1,upper])
        return res
