class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n =len(nums)
        nums.sort()

        cur=nums[0]
        t=1
        for i in nums[1:]:
            if i ==cur:
                t=t+1
                if t>n/2:
                    return i
            else:
                cur=i
                t=1

        return cur

