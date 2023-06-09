class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curMax=1
        curMin=1
        res=max(nums)
        for i in nums:
            if i!=0:
                t1=i*curMax
                t2=i*curMin
                curMax=max(t1,t2,i)
                curMin=min(t1,t2,i)
                res=max(res,curMax,curMin)
               
            else:
                curMax=1
                curMin=1

            

        return res
