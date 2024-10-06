class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        total=0
        res=math.inf

        l=0
        r=0
        while r<len(nums):

            total+=nums[r]
            print(total,l,r)
            if total<target:
                r=r+1
            else:
                res=min(res,r-l+1)
                while total>=target:
                    res=min(res,r-l+1)
                    total=total-nums[l]
                    l=l+1
                r=r+1

        if math.inf==res:
            return 0
        return res
                    