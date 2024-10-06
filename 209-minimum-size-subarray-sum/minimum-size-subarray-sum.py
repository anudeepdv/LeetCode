class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0 
        cur =0 
        res=math.inf
        for  r in range(len(nums)):
            cur  = cur +nums[r]
            print(cur)
            while cur>target:
                cur =cur - nums[l]
                res = min(res,r-l+1)
                l = l +1
            print(cur,"--")
            if cur == target:
                res = min(res,r-l+1)
            

        return res if res!=math.inf else 0