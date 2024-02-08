class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        res=math.inf
        for i in range(len(nums)-2):

            l=i+1
            r=len(nums)-1

            while l<r:
                val = nums[i]+nums[l]+nums[r]

                if val>target:
                    r=r-1
                else:
                    l=l+1

                if abs(val-target)<abs(target-res):
                    res = val

        return res