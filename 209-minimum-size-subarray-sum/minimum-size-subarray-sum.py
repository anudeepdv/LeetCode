class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l=0
        r=0
        s=0
        maxy=float('inf')
        for r in range(len(nums)):
            s = s+nums[r]

            while s>=target:
                maxy=min(maxy,r-l+1)
                s-=nums[l]
                l=l+1

        return maxy if maxy!=float('inf') else 0
