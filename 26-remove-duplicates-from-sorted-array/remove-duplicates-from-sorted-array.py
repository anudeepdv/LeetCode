class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i=0
        for x in nums[1:]:
            print(x,nums[i])
            if x!=nums[i]:
                nums[i+1]=x
                i=i+1
        print(nums)
        return i+1