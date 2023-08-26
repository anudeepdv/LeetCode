class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        res=max(nums)

        cmin,cmax=1,1

        for i in nums:
            if i==0:
                cmin,cmax=1,1
            else:

                temp =cmax
                cmax=max(i*cmin,i*cmax,i)
                cmin=min(i*cmin,i*temp,i)

                res=max(res,cmax)

        return res

