class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
       
        res = 0

        d={}
        pre=0
        for i, val in enumerate(nums):
            pre+=val

            if pre==k:
                res=i+1

            if pre - k in d:
                res=max(res,i-d[pre-k])

            if pre not in d:
                d[pre]=i


        return res
        